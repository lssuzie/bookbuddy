# 🎧 BookBuddy · AI读书伴侣

> **AI读书伴侣 — 把读书变成愉悦、享受、沉浸的体验。**
>
> 让读书变成一件你想做的事，而不是你应该做的事。
>
> 把你喜欢的任何文本，用你喜欢的任何声音，做成有声书。

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/bookbuddy.svg?style=flat-square)](https://github.com/lssuzie/bookbuddy/stargazers)

[中文](#-ai悦读) | [English](#-bookbuddy)

---

## 🇨🇳 AI读书伴侣

### 这是给谁用的？

**给你自己。** 如果你也有过这些瞬间：

- 买了一本书，翻了两页就吃灰了
- 觉得读书是"应该做的事"，而不是"想做的事"
- 盯着屏幕一整天，眼睛真的快废了
- 通勤/做饭/睡前想听点东西，但播客质量太随机

### 为什么会有这个工具

因为对自己有用。

你可能记得电影 *Her* 里的 Samantha——一个 AI，用她的声音走进了男主的生活，陪他读书、聊天、思考。

**声音可以是一种陪伴。**

BookBuddy 的想法很简单：如果你有一个喜欢的声音，用这个声音来读书，你会更愿意听，也更容易把一本书听完。

既然这个逻辑对你成立，那对很多人应该也成立——

> **用现有 AI 技术，打造最接近《Her》的阅读体验。**

Samantha 不是 TTS，她是陪伴。我们造不出她——但我们可以一步一步靠近。

- 追星的人可以用偶像的声音读书
- 学英语的人可以用喜欢的声音练听力
- 阅读困难的人可以换成听觉输入
- 眼睛累了的人可以让耳朵上岗

**读书的障碍从来不是书本身，是"开始读"的那一步。**

### 声音从哪里来

BookBuddy 支持四种方式：

| 方式 | 怎么做 |
|:----|:------|
| **🎤 内置音色** | 直接用，零准备 |
| **📝 克隆自己的声音** | 录 5 秒音频 → `--voice-clone` |
| **🎨 创造你喜欢的声线** | 选一个接近的参考音频 + 调 Prompt 反复打磨 |
| **🔊 克隆其他人的声音 ⚠️** | 有授权的参考音频 → `--voice-clone` |

**内置音色**来自 Mimo TTS 和微软 TTS，两者都有大量免费声音可用（男声、女声、各种风格）。
**创造声线**的意思是：没有现成的"低沉磁性"按钮，但你可以找一个接近的声音做参考，然后通过调整 Prompt（提示词）让输出的语气和质感越来越接近你想要的效果。

### 配置说明

BookBuddy 目前使用 **Mimo TTS** 作为后端引擎：

1. 去 [100t.xiaomimimo.com](https://100t.xiaomimimo.com/) 注册
2. 复制你的 API Key（`sk-` 开头）
3. 配置到环境变量：
   ```bash
   export MIMO_API_KEY="你的key"
   ```

Mimo TTS 提供免费额度，声音克隆和基础 TTS 都在同一个 API 里。未来会支持更多引擎（微软 TTS 等）。

### 它能做什么

```
一句话版：把 .txt / .md 文件变成有声书
--------

四个场景，一个工具：

1️⃣ 有声书（逐字朗读）
   # 用内置声音（Mimo / 微软TTS 提供多种预制音色，免费可用）
   python3 generate_audio.py 书.txt --clean

   # 克隆自己的声音（录 5 秒就够了）
   python3 generate_audio.py 书.txt --voice-clone --ref-audio 我的声音.mp3

   # 克隆其他人的声音⚠️（请确保你有使用权，见伦理承诺）
   python3 generate_audio.py 书.txt --voice-clone --ref-audio 参考音频.mp3

2️⃣ 学英语（用喜欢的声音练听力）
   # 英文文章 → 你喜欢的声音朗读 → 边听边看原文
   python3 generate_audio.py english_article.txt --clean
   python3 generate_audio.py english_article.txt --voice-clone --ref-audio 我的声音.mp3

3️⃣ AI代读播客（先总结再读）
   AI Agent 读完 → 口语化总结 → 转成播客
   适合小说集、论文集、读不完的大部头

4️⃣ 公版书一键下载+转有声书
   python3 generate_audio.py --download 道德经 --clean
   python3 generate_audio.py --download "tao te ching" --voice-clone --ref-audio 我的声音.mp3
```

### 快速开始

```bash
# 1. 安装依赖
brew install ffmpeg

# 2. 获取 API Key（免费额度）
#    去 https://100t.xiaomimimo.com/ 注册 → 复制你的 tp-xxx 开头的 Key
export MIMO_API_KEY="你的key"

# 3. 生成第一本有声书
python3 generate_audio.py 你的书.txt --clean
```

> 💡 **没有书？** 试试一键下载公版书：
> `python3 generate_audio.py --download 道德经 --clean`

> 💡 **想用自己的声音？** 录 5 秒音频：
> `python3 generate_audio.py 书.txt --voice-clone --ref-audio 我录的5秒.mp3`

> 💡 **声音可以选** — 内置几十种预制音色，可以克隆自己的，也可以设计你喜欢的声线（低沉、磁性、温柔...），全看你怎么用。

### 技术亮点

| 特性 | 为什么重要 |
|:----|:----------|
| **NFKC 清洗** | 修正 PDF/OCR 的乱码字，读出来不崩 |
| **智能分片 ≤100字** | 防止 TTS 长句读飘、吞音、电音 |
| **断点续传** | 中断了重跑，跳过已生成的，不白等 |
| **--download** | 搜公版书/Gutenberg，一键下载转有声书 |
| **声音克隆** | 用 5 秒录音克隆任何声线（用户自备参考音频） |
| **分卷合并** | 每 30 段自动合并，ffmpeg 成最终 MP3 |

### 伦理承诺

> 此工具是**个人工具**，不是内容分发平台。
>
> - **声音**：请只使用你自己的声音，或你已获授权的声音参考
> - **内容**：请只朗读你有权访问的文本（你自己的文章、公版书、已购电子书）
> - **禁止**：不要用此工具生成的内容冒充他人，不要用于商业盈利
>
> 工具本身是中立的。你用它做什么，是你的选择。

---

## 🇺🇸 BookBuddy

> **Your AI reading companion — Turn reading into pleasure, enjoyment, immersion.**
>
> Make reading something you *want* to do, not something you *should* do.
>
> Turn any text into an audiobook, in any voice you love.

### Who is this for?

**For yourself.** If you've ever:

- Bought a book and never opened it
- Felt reading was homework, not pleasure
- Stared at screens all day until your eyes hurt
- Wanted something good to listen to on your commute

### What it does

```bash
# Read a book with built-in voices (Mimo / Microsoft TTS, free)
python3 generate_audio.py my_book.txt --clean

# Voice clone (record 5 seconds of your voice / a voice you have rights to)
python3 generate_audio.py my_book.txt --voice-clone --ref-audio my_voice.mp3

# Download a public domain book + convert in one step
python3 generate_audio.py --download "tao te ching" --voice-clone --ref-audio my_voice.mp3
```

### Voice options

| Option | How |
|:------|:----|
| **🎤 Built-in voices** | Use directly, zero setup |
| **📝 Clone your own** | Record 5s → `--voice-clone` |
| **🎨 Design your voice** | Pick a reference + tune the prompt |
| **🔊 Clone others ⚠️** | Only with permission |

### Setup

1. Sign up at [100t.xiaomimimo.com](https://100t.xiaomimimo.com/)
2. Get your API Key (starts with `sk-`)
3. Set environment variable:
   ```bash
   export MIMO_API_KEY="your-key"
   ```

Mimo TTS has free credits included. Voice cloning and basic TTS use the same API.

### Ethical Commitment

> This is a **personal tool**, not a content platform.
>
> - **Voice**: Use only your own voice, or voices you have permission to use
> - **Content**: Read only text you have rights to access
> - **No**: Don't impersonate others, don't use for commercial purposes
>
> The tool is neutral. What you do with it is your choice.

---

## License

CC BY-NC-SA 4.0 — Free for personal use, no commercial use.
