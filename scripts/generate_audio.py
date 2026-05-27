import os
import sys
import re
import base64
import requests
import json
import subprocess
import shutil
import argparse

def get_mimo_key(env_path=None):
    """从环境变量或 .env 文件获取 MiMo API Key"""
    # 优先从环境变量读取
    if os.environ.get("MIMO_API_KEY"):
        return os.environ["MIMO_API_KEY"]

    # 搜索 .env 文件的候选路径
    candidates = []
    if env_path:
        candidates.append(env_path)
    candidates.extend([
        os.path.expanduser("~/.gemini/antigravity/scratch/.env"),
        os.path.expanduser("~/.mimo/.env"),
        os.path.expanduser("~/.env"),
    ])

    for path in candidates:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content.startswith("tp-") and len(content) > 20:
                    return content
                match = re.search(r"(tp-[a-zA-Z0-9]{15,})", content)
                if match:
                    return match.group(1)
    return None

def split_text(text, max_len=280):
    """按字数和段落切分文本。"""
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = []
    current_len = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if current_len + len(para) > max_len:
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = [para]
                current_len = len(para)
            else:
                chunks.append(para)
                current_chunk = []
                current_len = 0
        else:
            current_chunk.append(para)
            current_len += len(para) + 1

    if current_chunk:
        chunks.append("\n".join(current_chunk))
    return chunks

def text_to_speech_segment(text, index, api_key, temp_dir, voice_id="白桦", speed=1.0):
    url = "https://token-plan-cn.xiaomimimo.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    optimized_text = text.replace("。", "。， ")

    speed_instruction = "语速加快到1.2倍。" if speed == 1.2 else ""
    user_prompt = f"请用男声白桦朗读以下文字。注意：你的声音要磁性好听，同时请注入丰富且生动的感情，避免平淡无奇。请使用极其标准且规范的普通话，吐字要清晰有力、字字分明，避免任何含糊或吞音，不带口音。{speed_instruction}在句号等标点处，请保持清晰、较长且自然的停顿。"

    payload = {
        "model": "mimo-v2.5-tts",
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            },
            {
                "role": "assistant",
                "content": optimized_text
            }
        ],
        "audio": {
            "format": "mp3",
            "voice": voice_id,
            "speed": speed
        }
    }

    out_path = os.path.join(temp_dir, f"part_{index:04d}.mp3")

    for attempt in range(3):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=120)
            if response.status_code == 200:
                data = response.json()
                audio_b64 = data["choices"][0]["message"]["audio"]["data"]
                audio_bytes = base64.b64decode(audio_b64)
                with open(out_path, "wb") as f:
                    f.write(audio_bytes)
                print(f"✅ 分段 {index} 生成成功。")
                return out_path
            else:
                print(f"⚠️ 尝试 {attempt+1} 失败 (分段 {index}): HTTP {response.status_code} - {response.text}")
        except Exception as e:
            print(f"⚠️ 尝试 {attempt+1} 发生异常 (分段 {index}): {e}")

    raise Exception(f"❌ 无法在 3 次尝试后生成分段 {index}。")

def check_and_merge_chunks(temp_dir, total_segments, output_dir, book_name):
    """按每 30 段自动合并为一个分卷 MP3"""
    chunks = []
    start = 1
    while start <= total_segments:
        end = min(start + 29, total_segments)
        chunks.append((start, end))
        start += 30

    for start, end in chunks:
        output_filename = f"{book_name}_第{start:03d}到{end:03d}段.mp3"
        output_path = os.path.join(output_dir, output_filename)

        if os.path.exists(output_path):
            continue

        all_exist = True
        part_paths = []
        for idx in range(start, end + 1):
            part_path = os.path.join(temp_dir, f"part_{idx:04d}.mp3")
            if not (os.path.exists(part_path) and os.path.getsize(part_path) > 1024):
                all_exist = False
                break
            part_paths.append(part_path)

        if all_exist:
            print(f"\n🎵 检测到分段 {start} 到 {end} 已全部生成，正在自动合并为 {output_filename}...")
            filelist_path = os.path.join(temp_dir, f"filelist_{start}_{end}.txt")
            with open(filelist_path, "w", encoding="utf-8") as f:
                for part in part_paths:
                    f.write(f"file '{part}'\n")
            cmd = [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0",
                "-i", filelist_path, "-c", "copy", output_path
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"✅ 自动合并成功并保存至: {output_filename}")
            else:
                print(f"⚠️ 自动合并失败 ({output_filename}): {res.stderr}")
            if os.path.exists(filelist_path):
                os.remove(filelist_path)

def build_audiobook():
    parser = argparse.ArgumentParser(
        description="万物播客 — 文本/Markdown 转高质量有声书",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python generate_audio.py my_book.md
  python generate_audio.py my_book.md -o output.mp3 -v 白桦
  python generate_audio.py my_book.md --fast
  MIMO_API_KEY=tp-xxx python generate_audio.py my_book.md
        """
    )
    parser.add_argument("input", nargs="?", help="输入的 Markdown/TXT 文件路径")
    parser.add_argument("-o", "--output", help="输出 MP3 文件路径 (默认: <输入文件名>.mp3)")
    parser.add_argument("-v", "--voice", default="白桦", help="音色名称 (默认: 白桦)")
    parser.add_argument("--fast", action="store_true", help="使用 1.2 倍速生成")
    parser.add_argument("--env", help=".env 文件路径 (包含 MIMO API Key)")
    parser.add_argument("--temp-dir", help="临时文件目录 (默认: 系统临时目录下的 audio_parts)")

    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        print("\n❌ 错误: 请指定输入文件路径。")
        sys.exit(1)

    md_path = os.path.abspath(args.input)
    if not os.path.exists(md_path):
        print(f"❌ 错误: 找不到文件: {md_path}")
        sys.exit(1)

    # 输出路径：默认和输入文件同名，后缀改为 .mp3
    if args.output:
        output_mp3 = os.path.abspath(args.output)
    else:
        base = os.path.splitext(md_path)[0]
        output_mp3 = base + ".mp3"

    preferred_voice = args.voice

    # 临时目录
    if args.temp_dir:
        temp_dir = os.path.abspath(args.temp_dir)
    else:
        import tempfile
        temp_dir = os.path.join(tempfile.gettempdir(), "audiobook_parts")

    book_name = os.path.splitext(os.path.basename(md_path))[0]
    output_dir = os.path.dirname(output_mp3) or "."

    key = get_mimo_key(args.env)
    if not key:
        print("❌ 错误: 未找到 MiMo API Key。")
        print("   请通过以下方式之一提供：")
        print("   1. 环境变量: MIMO_API_KEY=tp-xxx")
        print("   2. .env 文件: --env /path/to/.env")
        print("   3. 放置在 ~/.gemini/antigravity/scratch/.env")
        sys.exit(1)

    print(f"📖 正在读取: {md_path}")

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # 去除 Markdown 格式标记
    clean_txt = md_content.replace("# ", "").replace("## ", "").replace("---", "")

    # 根据是否 --fast 决定分段策略
    if args.fast:
        # 快速模式：800 字分段，1.2 倍速
        segments = split_text(clean_txt, max_len=800)
        speed = 1.2
        print(f"🎬 快速模式: {len(segments)} 段, 1.2x 语速")
    else:
        # 标准模式：280 字分段，1.0 倍速
        segments = split_text(clean_txt, max_len=280)
        speed = 1.0
        print(f"🎬 标准模式: {len(segments)} 段, 1.0x 语速")

    os.makedirs(temp_dir, exist_ok=True)

    # 启动前先尝试对已存在的分段进行自动合并
    check_and_merge_chunks(temp_dir, len(segments), output_dir, book_name)

    part_files = []
    try:
        for idx, seg in enumerate(segments):
            part_filename = f"part_{(idx+1):04d}.mp3"
            part_path = os.path.join(temp_dir, part_filename)

            # 断点续传
            if os.path.exists(part_path) and os.path.getsize(part_path) > 1024:
                print(f"⏭️ 分段 {idx+1}/{len(segments)} 已存在，跳过。")
                part_files.append(part_path)
                continue

            print(f"🎙️ 正在转换分段 {idx+1}/{len(segments)} (字数: {len(seg)}, 语速: {speed}x)...")
            part_path = text_to_speech_segment(seg, idx+1, key, temp_dir, preferred_voice, speed)
            part_files.append(part_path)

            # 生成新分段后检查是否能合并新分卷
            check_and_merge_chunks(temp_dir, len(segments), output_dir, book_name)

        # 拼接最终音频
        print("🎵 正在使用 ffmpeg 合并音频...")
        filelist_path = os.path.join(temp_dir, "filelist.txt")
        with open(filelist_path, "w", encoding="utf-8") as f:
            for part in part_files:
                f.write(f"file '{part}'\n")

        cmd = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", filelist_path, "-c", "copy", output_mp3
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"\n🎉 完成! 音频已保存至: {output_mp3}")
            # 清理临时分段文件
            for part in part_files:
                os.remove(part)
            if os.path.exists(filelist_path):
                os.remove(filelist_path)
            print("✨ 临时文件已清理。")
        else:
            print(f"❌ 合并音频失败: {result.stderr}")

    except KeyboardInterrupt:
        print(f"\n⏸️ 已中断。已生成的分段保存在: {temp_dir}")
        print("   重新运行脚本即可断点续传。")
    except Exception as e:
        print(f"❌ 合成中断: {e}")
        print(f"💡 已生成的分段保存在: {temp_dir}，恢复后重新运行即可续传。")

if __name__ == "__main__":
    build_audiobook()
