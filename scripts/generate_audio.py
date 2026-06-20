#!/usr/bin/env python3
"""
万物播客 — 文本/Markdown 转高质量有声书 v2.1

三种模式：
  1. 基础 TTS（预制音色）：  默认，-v 白桦
  2. 声音克隆（零样本克隆）： --voice-clone --ref-audio 参考.mp3
  3. 公版书下载+自动转：    --download 道德经

一条命令搞定找书+转有声书：
  python generate_audio.py --download 道德经 -v 白桦
  python generate_audio.py --download 道德经 --voice-clone --ref-audio 我的声音.mp3

支持所有模式共用：清洗、智能分片、断点续传、自动分卷、ffmpeg 合并
"""

import os, sys, re, base64, requests, subprocess, argparse, unicodedata, tempfile

# ============================================================
# API 配置
# ============================================================

# 公版书籍下载源
GUTENBERG_SEARCH = "https://www.gutenberg.org/ebooks/search/?query="
GUTENBERG_TEXT   = "https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"

# 常见公版书直接映射（避免依赖搜索）
KNOWN_BOOKS = {
    "道德经":   ["216", "Tao Te Ching（英译）"],
    "tao te ching": ["216", "Tao Te Ching"],
    "孙子兵法": ["17468", "Sunzi's Art of War（英译）"],
    "art of war":  ["17468", "The Art of War"],
    "论语":     ["7337", "Analects of Confucius（英译）"],
    "analects":    ["7337", "The Analects"],
}
TTS_API_URL    = "https://token-plan-cn.xiaomimimo.com/v1/chat/completions"
CLONE_API_URL  = "https://api.xiaomimimo.com/v1/chat/completions"

# 声音克隆提示词预设
CLONE_PROMPTS = {
    "有声书":   "用平静沉稳的旁白语气朗读，像是在给听众讲故事。语速适中，情感自然。不要过于戏剧化，保持克制。",
    "标准流利": "用极其自然、连贯流畅的旁白语调进行朗读，像是在用温暖的普通话给好朋友讲故事，注入饱满、温和且生动的感情。不要有任何刻意的停顿。保持语气连贯顺畅，字与字之间自然衔接，避免一字一顿的呆板感。",
    "深夜":     "用随性、平静、毫无修饰的自然语调朗读，像是在私底下和老朋友聊天。语气诚恳、谦逊，不要播音腔。",
}

# ============================================================
# 工具函数
# ============================================================

def get_mimo_key(env_path=None):
    """从环境变量或 .env 文件获取 MiMo API Key"""
    if os.environ.get("MIMO_API_KEY"):
        return os.environ["MIMO_API_KEY"]

    candidates = [env_path] if env_path else []
    candidates.extend([
        os.path.expanduser("~/.gemini/antigravity/scratch/.env"),
        os.path.expanduser("~/.mimo/.env"),
        os.path.expanduser("~/.env"),
    ])
    for path in candidates:
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content.startswith("tp-") and len(content) > 20:
                    return content
                match = re.search(r"(tp-[a-zA-Z0-9]{15,})", content)
                if match:
                    return match.group(1)
    return None


def clean_text(text):
    """全面的文档清洗：分隔线、URL、硬换行、NFKC"""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r'^[=\-*]{4,}\s*$', '', text, flags=re.MULTILINE)   # 分隔线
    text = re.sub(r'\[全文完\]', '', text)                              # 标签
    text = re.sub(r'https?://\S+', '', text)                            # URL
    text = text.replace('→', '').replace('←', '')

    # 合并硬换行
    lines = text.split('\n')
    merged = []
    for line in lines:
        s = line.strip()
        if not s:
            if merged and merged[-1] != '':
                merged.append('')
            continue
        if merged and merged[-1] != '':
            prev = merged[-1]
            if prev[-1] not in '。？！」」』）':
                merged[-1] = prev + s
            else:
                merged.append(s)
        else:
            merged.append(s)
    text = '\n'.join(merged)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'  +', ' ', text)
    return text.strip()


def split_text(text, max_len=100):
    """按句子切分文本，每段不超过 max_len 字"""
    sentences = re.split(r'(?<=[。？！\n])', text)
    chunks, current = [], []
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        if len(sent) > max_len:
            if current:
                chunks.append("".join(current))
                current = []
            chunks.append(sent)
            continue
        combined = "".join(current) + sent
        if len(combined) > max_len and current:
            chunks.append("".join(current))
            current = [sent]
        else:
            current.append(sent)
    if current:
        chunks.append("".join(current))
    return chunks


def download_book(query):
    """搜索并下载公版书籍。支持已知公版书、Gutenberg、直接 URL。
    返回 (文件路径, 书名) 或 (None, 错误信息)。"""
    import urllib.request, urllib.parse
    q = query.lower().strip()

    # --- 如果是直接 URL ---
    if query.startswith("http://") or query.startswith("https://"):
        print(f"  🌐 下载: {query}")
        resp = requests.get(query, timeout=30)
        resp.encoding = "utf-8"
        name = re.sub(r'[\\/:*?"<>|]', "_", query.split("/")[-1].split("?")[0]) or "downloaded"
        # 防止 pg216.txt.txt
        base, ext = os.path.splitext(name)
        if ext == ".txt":
            out = name
        else:
            out = f"{name}.txt"
        with open(out, "w", encoding="utf-8") as f:
            f.write(resp.text)
        print(f"  ✅ 已保存: {out} ({len(resp.text)} 字)")
        return out, name

    print(f"🔍 搜索: {query}")

    # --- 1. 查已知公版书映射表 ---
    if q in KNOWN_BOOKS:
        book_id, title = KNOWN_BOOKS[q]
        url = GUTENBERG_TEXT.format(id=book_id)
        print(f"  📖 已知公版书: 《{title}》")
        return _download_gutenberg(url, book_id, title)

    # --- 2. 遍历映射表的 key 做模糊匹配 ---
    for key, (book_id, title) in KNOWN_BOOKS.items():
        if key in q or q in key:
            url = GUTENBERG_TEXT.format(id=book_id)
            print(f"  📖 匹配到公版书: 《{title}》")
            return _download_gutenberg(url, book_id, title)

    # --- 3. 搜索 Project Gutenberg ---
    try:
        search_url = GUTENBERG_SEARCH + urllib.parse.quote(query)
        resp = requests.get(search_url, timeout=15,
                            headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            ids = re.findall(r'/ebooks/(\d+)', resp.text)
            if ids:
                book_id = ids[0]
                url = GUTENBERG_TEXT.format(id=book_id)
                print(f"  📖 从 Gutenberg 搜索到 ID: {book_id}")
                return _download_gutenberg(url, book_id, query)
    except Exception as e:
        print(f"  ⚠️ Gutenberg 搜索失败: {e}")

    return None, (
        f"未找到「{query}」的公开电子版。\n"
        "  建议：\n"
        "  1. 直接传 URL: --download https://example.com/book.txt\n"
        "  2. 提供本地文件: python3 generate_audio.py 书.txt\n"
        "  3. 如果是中文古籍，试试英文名: --download 'tao te ching'"
    )


def _download_gutenberg(url, book_id, title):
    """从 Gutenberg 下载文本，提取书名。"""
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return None, f"Gutenberg 下载失败 (HTTP {resp.status_code})"
        resp.encoding = "utf-8"
        content = resp.text
        title_m = re.search(r'Title:\s*(.+)', content)
        nice_title = title_m.group(1).strip() if title_m else title
        out_name = re.sub(r'[\\/:*?"<>|]', "_", nice_title)
        out_path = f"{out_name}.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ 已保存: {out_path} ({len(content)} 字)")
        return out_path, nice_title
    except Exception as e:
        return None, f"下载失败: {e}"


def build_voice_clone_payload(text, ref_audio_path, prompt, speed=1.0, out_fmt="mp3"):
    """构造声音克隆请求 payload"""
    with open(ref_audio_path, "rb") as f:
        ref_bytes = f.read()
    ext = os.path.splitext(ref_audio_path)[1].lower()
    mime = "audio/mp3" if ext == ".mp3" else "audio/wav"
    return {
        "model": "mimo-v2.5-tts-voiceclone",
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": text},
        ],
        "audio": {
            "format": out_fmt,
            "voice": f"data:{mime};base64,{base64.b64encode(ref_bytes).decode()}",
            "speed": speed,
        }
    }


def build_tts_payload(text, voice_id, speed=1.0, out_fmt="mp3"):
    """构造基础 TTS 请求 payload"""
    optimized = text.replace("。", "。， ")
    speed_ins = "语速加快到1.2倍。" if speed == 1.2 else ""
    user_prompt = (
        f"请用男声{voice_id}朗读以下文字。注意：你的声音要磁性好听，"
        f"同时请注入丰富且生动的感情，避免平淡无奇。请使用极其标准且规范的普通话，"
        f"吐字要清晰有力、字字分明，避免任何含糊或吞音，不带口音。"
        f"{speed_ins}在句号等标点处，请保持清晰、较长且自然的停顿。"
    )
    return {
        "model": "mimo-v2.5-tts",
        "messages": [
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": optimized},
        ],
        "audio": {
            "format": out_fmt,
            "voice": voice_id,
            "speed": speed,
        }
    }


def call_tts(text, index, api_key, temp_dir, mode, **kwargs):
    """
    通用 TTS 调用入口。
    mode='tts':    kwargs 需含 voice_id, speed
    mode='clone':  kwargs 需含 ref_audio, prompt, speed
    """
    if mode == "clone":
        url = CLONE_API_URL
        payload = build_voice_clone_payload(text, kwargs["ref_audio"], kwargs["prompt"],
                                            kwargs.get("speed", 1.0))
    else:
        url = TTS_API_URL
        payload = build_tts_payload(text, kwargs["voice_id"], kwargs.get("speed", 1.0))

    out_path = os.path.join(temp_dir, f"part_{index:04d}.mp3")

    for attempt in range(3):
        try:
            resp = requests.post(
                url,
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json=payload,
                timeout=120
            )
            if resp.status_code == 200:
                audio = base64.b64decode(resp.json()["choices"][0]["message"]["audio"]["data"])
                with open(out_path, "wb") as f:
                    f.write(audio)
                print(f"  ✅ [{index:04d}] ({len(text)}字, {len(audio)/1024:.0f}KB)")
                return out_path
            else:
                print(f"  ⚠️ 尝试 {attempt+1} 失败 [{index}]: HTTP {resp.status_code}", end="")
                if attempt < 2:
                    print(" 重试...")
        except Exception as e:
            print(f"  ⚠️ 尝试 {attempt+1} 异常 [{index}]: {e}", end="")
            if attempt < 2:
                print(" 重试...")

    print(f"  ❌ [{index}] 3次尝试均失败")
    return None


def merge_volumes(temp_dir, total_segments, output_dir, book_name):
    """按每 30 段自动合并为一个分卷 MP3"""
    volumes = []
    for start in range(1, total_segments + 1, 30):
        end = min(start + 29, total_segments)
        vol_name = f"{book_name}_分卷{start//30+1:02d}(第{start}到{end}段).mp3"
        vol_path = os.path.join(output_dir, vol_name)

        parts = []
        for i in range(start, end + 1):
            p = os.path.join(temp_dir, f"part_{i:04d}.mp3")
            if os.path.exists(p) and os.path.getsize(p) > 1024:
                parts.append(p)

        if not parts:
            continue

        if os.path.exists(vol_path):
            volumes.append(vol_path)
            continue

        filelist = os.path.join(temp_dir, f"vol_{start}.txt")
        with open(filelist, "w") as f:
            for p in parts:
                f.write(f"file '{p}'\n")

        res = subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", filelist, "-c", "copy", vol_path],
            capture_output=True, text=True
        )
        os.remove(filelist)
        if res.returncode == 0:
            print(f"  📦 分卷: {vol_name}")
            volumes.append(vol_path)
        else:
            print(f"  ⚠️ 分卷合并失败: {res.stderr}")
    return volumes


def final_merge(volumes, output_path, temp_dir):
    """合并全部分卷为最终文件"""
    if not volumes:
        return None
    if len(volumes) == 1:
        os.rename(volumes[0], output_path)
        return output_path

    filelist = os.path.join(temp_dir, "final.txt")
    with open(filelist, "w") as f:
        for v in volumes:
            f.write(f"file '{v}'\n")
    res = subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", filelist, "-c", "copy", output_path],
        capture_output=True, text=True
    )
    os.remove(filelist)
    if res.returncode == 0:
        return output_path
    print(f"❌ 最终合并失败: {res.stderr}")
    return None


# ============================================================
# CLI
# ============================================================

def build_parser():
    p = argparse.ArgumentParser(
        description="万物播客 v2 — 文本转高质量有声书（支持基础TTS / 声音克隆）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
模式示例:
  # 基础 TTS（预制音色）
  python generate_audio.py 书.md
  python generate_audio.py 书.md -v 女声少女 --fast

  # 声音克隆（零样本克隆）
  python generate_audio.py 书.md --voice-clone --ref-audio 参考.mp3
  python generate_audio.py 书.md --voice-clone --ref-audio 参考.mp3 --clone-prompt 标准流利

  # 带文档清洗
  python generate_audio.py 书.txt --clean --voice-clone --ref-audio 参考.mp3

  # 指定 API Key
  MIMO_API_KEY=tp-xxx python generate_audio.py 书.md

  # 公版书籍下载 + 有声书（一步到位）
  python generate_audio.py --download 道德经
  python generate_audio.py --download 道德经 -o 道德经.mp3 -v 白桦
  python generate_audio.py --download 道德经 --voice-clone --ref-audio 我的声音.mp3
        """
    )
    p.add_argument("input", nargs="?", help="输入文本文件路径 (.txt / .md)，与 --download 二选一")
    p.add_argument("-o", "--output", help="输出 MP3 文件路径")

    # 下载 / 输入源
    p.add_argument("--download", help="搜索并下载公版书籍（如：道德经、论语）或直接 URL，与 input 二选一")
    p.add_argument("--download-only", action="store_true",
                   help="只下载书籍到 txt，不生成音频")
    p.add_argument("--voice-clone", action="store_true",
                   help="启用声音克隆模式（默认: 基础 TTS）")
    p.add_argument("--ref-audio", help="声音克隆参考音频路径")

    # 音色 / 风格
    p.add_argument("-v", "--voice", default="白桦",
                   help="基础TTS音色名称 (默认: 白桦)")
    p.add_argument("--clone-prompt", default="有声书",
                   choices=list(CLONE_PROMPTS.keys()) + ["自定义"],
                   help="声音克隆朗读风格 (默认: 有声书)")
    p.add_argument("--clone-prompt-text", default="",
                   help="自定义声音克隆提示词（当 --clone-prompt=自定义 时使用）")

    # 速度
    p.add_argument("--fast", action="store_true",
                   help="快速模式 (1.2x 语速 + 200字分段)")
    p.add_argument("-s", "--speed", type=float, default=None,
                   help="语速倍率 (覆盖 --fast 的默认速度)")

    # 处理选项
    p.add_argument("--clean", action="store_true",
                   help="启用文档清洗 (NFKC + 去分隔线/URL/硬换行)")
    p.add_argument("--env", help=".env 文件路径")
    p.add_argument("--temp-dir", help="临时文件目录")
    p.add_argument("--no-cleanup", action="store_true",
                   help="保留临时分段文件")
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    # ---- 校验：input 和 --download 二选一 ----
    if not args.input and not args.download:
        print("❌ 请指定输入文件路径 或使用 --download 下载公版书籍")
        parser.print_help()
        sys.exit(1)

    # ---- 如果指定了 --download ----
    if args.download:
        file_path, book_title_or_err = download_book(args.download)
        if not file_path:
            print(f"❌ {book_title_or_err}")
            sys.exit(1)
        if args.download_only:
            print(f"\n📄 仅下载完成: {file_path}")
            return
        # 用下载的文件作为输入
        args.input = file_path
        # 如果没有指定输出路径，以书名为基准
        if not args.output:
            args.output = f"{re.sub(r'[\\/:*?"<>|]', '_', book_title_or_err)}.mp3"

    # ---- 校验输入文件 ----
    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"❌ 找不到文件: {input_path}")
        sys.exit(1)

    if args.voice_clone and not args.ref_audio:
        print("❌ 声音克隆模式需要 --ref-audio 参数")
        sys.exit(1)
    if args.voice_clone and not os.path.exists(args.ref_audio):
        print(f"❌ 找不到参考音频: {args.ref_audio}")
        sys.exit(1)

    # ---- API Key ----
    api_key = get_mimo_key(args.env)
    if not api_key:
        print("❌ 未找到 MiMo API Key")
        print("   请设置环境变量 MIMO_API_KEY 或通过 --env 提供 .env 文件")
        sys.exit(1)

    # ---- 输出路径 ----
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        base = os.path.splitext(input_path)[0]
        suffix = "_clone" if args.voice_clone else ""
        output_path = f"{base}{suffix}.mp3"

    output_dir = os.path.dirname(output_path) or "."
    book_name = os.path.splitext(os.path.basename(input_path))[0]

    # ---- 临时目录 ----
    temp_dir = os.path.abspath(args.temp_dir) if args.temp_dir else \
               os.path.join(tempfile.gettempdir(), f"audiobook_{book_name}")
    os.makedirs(temp_dir, exist_ok=True)

    # ---- 读取 + 清洗 ----
    print(f"📖 读取: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        raw = f.read()

    if args.clean:
        text = clean_text(raw)
        print(f"   🧹 清洗: {len(raw)} → {len(text)} 字")
    else:
        text = raw.replace("# ", "").replace("## ", "").replace("---", "")
        print(f"   📄 原文: {len(text)} 字（未清洗）")

    # ---- 分段 ----
    max_len = 200 if args.fast else 100
    segments = split_text(text, max_len=max_len)
    speed = args.speed or (1.2 if args.fast else 1.0)
    mode_label = "声音克隆" if args.voice_clone else "基础TTS"
    print(f"📊 分段: {len(segments)} 段 (≤{max_len}字), {mode_label}, {speed}x")

    # ---- 提示词 ----
    if args.voice_clone:
        if args.clone_prompt == "自定义" and args.clone_prompt_text:
            prompt_text = args.clone_prompt_text
        else:
            prompt_text = CLONE_PROMPTS.get(args.clone_prompt, CLONE_PROMPTS["有声书"])
        print(f"🎤 参考音频: {args.ref_audio}")
        print(f"🎤 朗读风格: {args.clone_prompt}")
    else:
        prompt_text = ""
        print(f"🎤 音色: {args.voice}")

    # ---- 批量合成 ----
    part_files = []
    try:
        for idx, seg in enumerate(segments, 1):
            part_path = os.path.join(temp_dir, f"part_{idx:04d}.mp3")

            # 断点续传
            if os.path.exists(part_path) and os.path.getsize(part_path) > 1024:
                print(f"  ⏭️ [{idx:04d}] 已存在，跳过")
                part_files.append(part_path)
                continue

            print(f"🎙️ [{idx}/{len(segments)}]", end="")
            if args.voice_clone:
                result = call_tts(seg, idx, api_key, temp_dir, "clone",
                                  ref_audio=args.ref_audio, prompt=prompt_text, speed=speed)
            else:
                result = call_tts(seg, idx, api_key, temp_dir, "tts",
                                  voice_id=args.voice, speed=speed)

            if result:
                part_files.append(result)
                # 每生成一段检查是否可以合并分卷
                merge_volumes(temp_dir, len(segments), output_dir, book_name)
            else:
                print(f"  ⚠️ [{idx}] 跳过")

        # ---- 合并 ----
        print(f"\n📦 合并分卷...")
        volumes = merge_volumes(temp_dir, len(segments), output_dir, book_name)

        print(f"🔗 最终合并...")
        result = final_merge(volumes, output_path, temp_dir)

        if result:
            dur = subprocess.run(
                ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                 "-of", "csv=p=0", result],
                capture_output=True, text=True
            ).stdout.strip()
            print(f"\n🎉 完成！")
            print(f"   📁 {result}")
            print(f"   ⏱  {float(dur)/60:.0f} 分 {float(dur)%60:.0f} 秒" if dur else "")
            print(f"   📦 {os.path.getsize(result)/1024/1024:.1f} MB")
        else:
            print("❌ 合并失败")

    except KeyboardInterrupt:
        print(f"\n⏸️ 中断。分段保存在: {temp_dir}，重跑自动续传")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print(f"💡 分段保存在: {temp_dir}，重跑自动续传")

    # ---- 清理 ----
    if not args.no_cleanup and os.path.exists(temp_dir):
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
        print("✨ 临时文件已清理")


if __name__ == "__main__":
    main()