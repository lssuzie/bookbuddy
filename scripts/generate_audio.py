import os
import sys
import re
import base64
import requests
import json
import subprocess
import shutil

def get_mimo_key():
    env_path = "/Users/lushu/.gemini/antigravity/scratch/.env"
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content.startswith("tp-") and len(content) > 20:
                return content
            match = re.search(r"(tp-[a-zA-Z0-9]{15,})", content)
            if match:
                return match.group(1)
    return None

def split_text(text, max_len=280):
    """
    按字数和段落切分文本。
    """
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
    user_prompt = f"请用男声白桦朗读以下文字。注意：你的声音要磁性好听，同时请注入丰富且生动的感情，带有悬疑探案小说的叙事张力与情绪起伏，避免平淡无奇。请使用极其标准且规范的普通话，吐字要清晰有力、字字分明，避免任何含糊或吞音，不带口音。{speed_instruction}在句号等标点处，请保持清晰、较长且自然的停顿。"
    
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

def check_and_merge_chunks(temp_dir, total_segments, output_dir="/Users/lushu/Documents/爱呀河有声书"):
    # 第 1 卷为 1-22 段，此后每 30 段为一个独立 MP3 文件
    chunks = [(1, 22)]
    start = 23
    while start <= total_segments:
        end = min(start + 29, total_segments)
        chunks.append((start, end))
        start += 30
        
    for start, end in chunks:
        output_filename = f"爱呀河谜案录 有声书_第{start:03d}到{end:03d}段.mp3" if start > 1 else "爱呀河谜案录 有声书_第001到022段.mp3"
        output_path = os.path.join(output_dir, output_filename)
        
        # 若已合并过该部分，则跳过
        if os.path.exists(output_path):
            continue
            
        # 检查当前分卷的所有分段是否均已下载就绪
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
                print(f"✅ 自动合并成功并保存至专属文件夹: {output_filename}")
            else:
                print(f"⚠️ 自动合并失败 ({output_filename}): {res.stderr}")
            if os.path.exists(filelist_path):
                os.remove(filelist_path)

def build_audiobook():
    md_path = "/Users/lushu/Documents/爱呀河有声书/爱呀河谜案录 短篇集（全文）.md"
    output_mp3 = "/Users/lushu/Documents/爱呀河有声书/爱呀河谜案录 有声书.mp3"
    preferred_voice = "白桦"
    
    # 动态支持命令行传参：generate_audio.py [输入路径] [输出路径] [音色名]
    if len(sys.argv) >= 2:
        md_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_mp3 = sys.argv[2]
    if len(sys.argv) >= 4:
        preferred_voice = sys.argv[3]

    scratch_dir = "/Users/lushu/.gemini/antigravity/scratch"
    temp_dir = os.path.join(scratch_dir, "temp_audio_parts")
    
    key = get_mimo_key()
    if not key:
        print("❌ 错误: 未能在 .env 中找到有效的 MIMO_API_KEY。")
        return
        
    if not os.path.exists(md_path):
        print(f"❌ 错误: 找不到 Markdown 文件: {md_path}")
        return
        
    print("正在读取和清洗 Markdown 文本内容...")
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    # 去除 Markdown 格式标记以获得纯文本
    clean_txt = md_content.replace("# ", "").replace("## ", "").replace("---", "")
    
    # 根据用户要求，前 7 个分段保持原 800 字/1.2倍速规格，后面的部分使用 280 字/1.0倍速规格
    old_segments = split_text(clean_txt, max_len=800)
    first_part_segs = old_segments[:7]
    remaining_text = "\n\n".join(old_segments[7:])
    
    # 后面部分采用更短的 280 字分段规格
    new_segments = split_text(remaining_text, max_len=280)
    segments = first_part_segs + new_segments
    
    print(f"🎬 全书共划分为 {len(segments)} 个音频分段进行转换:")
    print(f"   - 前面 1-7 分段：保持已生成的 1.2倍速 (800字规格)")
    print(f"   - 后续 8-{len(segments)} 分段：使用 1.0倍速 清晰版 (280字规格)")
    
    # 每次运行前，不需要重复清理缓存，断点续传会自动跳过已生成的文件。
    os.makedirs(temp_dir, exist_ok=True)
    part_files = []
    
    # 启动前先尝试对已存在的分段进行自动合并
    check_and_merge_chunks(temp_dir, len(segments))
    
    try:
        for idx, seg in enumerate(segments):
            part_filename = f"part_{(idx+1):04d}.mp3"
            part_path = os.path.join(temp_dir, part_filename)
            
            # 断点续传
            if os.path.exists(part_path) and os.path.getsize(part_path) > 1024:
                print(f"⏭️ 分段 {idx+1}/{len(segments)} 已存在，直接跳过。")
                part_files.append(part_path)
                continue
                
            speed = 1.2 if (idx < 7) else 1.0
            print(f"🎙️ 正在转换分段 {idx+1}/{len(segments)} (字数: {len(seg)}, 语速: {speed}x)...")
            part_path = text_to_speech_segment(seg, idx+1, key, temp_dir, preferred_voice, speed)
            part_files.append(part_path)
            
            # 生成新分段后检查是否能合并新分卷
            check_and_merge_chunks(temp_dir, len(segments))
            
        # 拼接音频
        print("🎵 正在使用 ffmpeg 无损合并音频分段...")
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
            print(f"\n🎉 恭喜! 完整有声书已成功合成并保存至: {output_mp3}")
            for part in part_files:
                os.remove(part)
            os.remove(filelist_path)
            os.rmdir(temp_dir)
            print("✨ 临时文件已清理完毕。")
        else:
            print(f"❌ 合并音频时 ffmpeg 报错: {result.stderr}")
            
    except Exception as e:
        print(f"❌ 有声书合成中断: {e}")
        print("💡 提示: 已经成功生成的分段已保存在缓存中，恢复网络后重新运行脚本即可断点续传。")

if __name__ == "__main__":
    build_audiobook()
