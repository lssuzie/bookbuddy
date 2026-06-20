# 🎧 Everything-to-Podcast

> **让读书变成一件你想做的事，而不是你应该做的事。**
>
> 把你喜欢的任何文本，用你喜欢的任何声音，做成有声书。

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/everything-to-podcast.svg?style=flat-square)](https://github.com/lssuzie/everything-to-podcast/stargazers)

[中文](#-万物播客) | [English](#-everything-to-podcast)

---

## 🇨🇳 万物播客

### 这是给谁用的？

**给你自己。** 如果你也有过这些瞬间：

- 买了一本书，翻了两页就吃灰了
- 觉得读书是"应该做的事"，而不是"想做的事"
- 盯着屏幕一整天，眼睛真的快废了
- 通勤/做饭/睡前想听点东西，但播客质量太随机

### 为什么会有这个工具

因为对自己有用。

我很喜欢梁朝伟。如果用他的声音来读书，我会更愿意听，也会更容易把一本书听完。既然这个逻辑对我成立，那对很多人应该也成立——

- 追星的人可以用偶像的声音读书
- 学英语的人可以用喜欢的声音练听力
- 阅读困难的人可以换成听觉输入
- 眼睛累了的人可以让耳朵上岗

**读书的障碍从来不是书本身，是"开始读"的那一步。**

### 它能做什么

```
一句话版：把 .txt / .md 文件变成有声书
--------

支持三种用法：

1️⃣ 有声书（逐字朗读）
   python3 generate_audio.py 书.txt --clean -v 白桦
   python3 generate_audio.py 书.txt --voice-clone --ref-audio 我的声音.mp3

2️⃣ AI代读播客（先总结再读）
   AI Agent 读完 → 口语化总结 → 转成播客
   适合小说集、论文集、读不完的大部头

3️⃣ 公版书一键下载+转有声书
   python3 generate_audio.py --download 道德经 -v 白桦
   python3 generate_audio.py --download "tao te ching" --voice-clone --ref-audio 我的声音.mp3
```

### 快速开始

```bash
# 1. 安装依赖
brew install ffmpeg

# 2. 配好 API Key
export MIMO_API_KEY="你的key"   # 去 https://100t.xiaomimimo.com/ 申请

# 3. 生成有声书
python3 generate_audio.py 你的书.txt --clean -v 白桦
```

更详细的用法见 [`scripts/generate_audio.py --help`](scripts/generate_audio.py)。

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

## 🇺🇸 Everything-to-Podcast

> **Make reading something you *want* to do, not something you *should* do.**
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
# Read a book with built-in voices
python3 generate_audio.py my_book.txt --clean -v 白桦

# Voice clone (record 5 seconds of your voice / a voice you have rights to)
python3 generate_audio.py my_book.txt --voice-clone --ref-audio my_voice.mp3

# Download a public domain book + convert in one step
python3 generate_audio.py --download "tao te ching" --voice-clone --ref-audio my_voice.mp3
```

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
