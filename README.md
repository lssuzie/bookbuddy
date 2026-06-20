# 🎧 BookBuddy · AI读书伴侣

> **AI读书伴侣 - 把读书变成愉悦、享受、沉浸的体验。**
>
> 让读书变成一件你想做的事，而不是你应该做的事。
>
> 把你喜欢的任何文本，用你喜欢的任何声音，做成有声书。

![Demo](https://raw.githubusercontent.com/lssuzie/bookbuddy/master/demo.gif)

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/bookbuddy.svg?style=flat-square)](https://github.com/lssuzie/bookbuddy/stargazers)

[中文](#-ai悦读) | [English](#-bookbuddy)

---

## 🇨🇳 AI读书伴侣

### 你也有过这些瞬间吗?

- 买了一本书,翻了两页就吃灰了
- 觉得读书是"应该做的事",而不是"想做的事"
- 盯着屏幕一整天,眼睛真的快废了
- 通勤/做饭/睡前想听点东西,但播客质量太随机

### AI 时代,应该有新的读书方式

我们生活在一个信息爆炸的时代,但读书的方式却停留在几百年前--打开书,盯着字,一个字一个字读。

**AI 时代,读书应该更私密、更定制化、更沉浸式、更友好。**

- **更私密**:你的书,你的声音,你的节奏。没有算法推荐,没有社交压力,只有你和文字。
- **更定制化**:用你喜欢的声音读你喜欢的书。可以是你的声音,可以是偶像的声音,可以是任何你愿意听的声音。
- **更沉浸式**:闭上眼睛,让声音把你带入文字的世界。像听一个人坐在你身边,轻声细语地读给你听。
- **更友好**:眼睛累了就让耳朵上岗,时间不够就边通勤边听,读不进去就换个声音试试。

读书的障碍从来不是书本身,是"开始读"的那一步。把读书变成听觉体验,把"应该读"变成"想听"。

### 传统有声书 vs AI 有声书

传统有声书最大的问题:**你只能听别人选的声音。**

|  | 传统有声书 | AI 有声书 (BookBuddy) |
|:----|:----|:----|
| **声音** | 固定的,你无法选择 | 你可以选:自己的声音、偶像的声音、任何你喜欢的声音 |
| **语气** | 固定的,你无法调整 | 你可以调:语速、情感、风格、甚至让声音带点沙哑或气息感 |
| **内容** | 只有畅销书有 | 任何文本都能转:你自己的笔记、PDF、网页、论文 |
| **更新** | 作者什么时候录什么时候有 | 随时生成,想听就听 |
| **成本** | 买一本几十块 | 免费(Mimo 提供免费额度) |

**AI 时代,读书应该是一种高度个人化的体验。** 不是"这本书有人读吗",而是"我想用什么样的声音读这本书"。

### 声音,可以是一种陪伴

你可能记得电影 *Her* 里的 Samantha--一个 AI,用她的声音走进了男主的生活,陪他读书、聊天、思考。

**BookBuddy 的想法很简单:如果你有一个喜欢的声音,用这个声音来读书,你会更愿意听,也更容易把一本书听完。**

我们暂时还造不出一个像 Samantha 那样完整的 AI 伴侣--那种能真正理解你、回应你、和你一起生活的存在。但我们可以从声音开始,用声音实现那种陪伴感。

**一个声音一直在你身边,陪你读一本书。** 这就是 BookBuddy 目前做到的--有声书。

读书的障碍从来不是书本身,是"开始读"的那一步。把读书变成听觉体验,把"应该读"变成"想听"。

- 眼睛累了的人可以让耳朵上岗
- 通勤/睡前想听点东西的人可以换种方式阅读
- 阅读困难的人可以换成听觉输入
- 学英语的人可以用喜欢的声音练听力

### 我们暂时还造不出 Samantha,但可以从声音开始靠近

> **用现有 AI 技术,把读书变成愉悦、享受、沉浸的体验。**

Samantha 不是 TTS,她是陪伴。完整的 AI 伴侣系统我们还造不出--但我们可以从声音开始,一步一步靠近。一个声音一直在你身边,陪你读一本书。这就是 BookBuddy 目前做到的。

### 三种模式,三种声音来源

| 模式 | 怎么做 | 适合谁 |
|:----|:------|:------|
| **🎤 内置音色** | 直接用,零准备 | 想先试试的人 |
| **🎨 声音设计** | 用文字描述创造声线 → `--voice-design "低沉磁性的男声"` | 想要定制但没参考音频的人 |
| **📝 声音克隆** | 录 5 秒音频 → `--voice-clone --ref-audio` | 想用自己的声音/有参考音频的人 |

#### 内置音色一览(Mimo TTS)

| 音色 | 语言 | 性别 | 感觉 |
|:----|:----:|:----:|:----|
| 冰糖 | 中文 | 女 | 清亮甜美 |
| 茉莉 | 中文 | 女 | 温柔知性 |
| 苏打 | 中文 | 男 | 清爽活力 |
| 白桦 | 中文 | 男 | 沉稳磁性 |
| Mia | 英文 | 女 | Bright |
| Chloe | 英文 | 女 | Warm |
| Milo | 英文 | 男 | Deep |
| Dean | 英文 | 男 | Calm |

#### 声音设计:写一段话,就能创造一种声音

不需要找参考音频,直接用文字描述你想要的声音:

```bash
# 睡前催眠模式(内置预设)
python generate_audio.py 书.txt --voice-design "睡前催眠"

# Her 知性元气(内置预设) - 温暖沙哑气息感女声,贴耳私语风格
python generate_audio.py 书.txt --voice-design "Her 知性元气"

# 自定义:低沉磁性的深夜电台男声
python generate_audio.py 书.txt --voice-design "低沉磁性的中年男声,像深夜电台主播"

# 自定义:元气明亮的励志声线
python generate_audio.py 书.txt --voice-design "元气明亮的少年音" \
  --design-prompt "用充满朝气的语气朗读,语速轻快"
```

**内置预设**:睡前催眠 / 冥想引导 / 深夜电台 / 温柔叙述 / Her 知性元气

**支持描述维度**:性别、年龄、声线质感(磁性/沙哑/清亮)、情绪(温暖/沉稳/元气)、语速、角色(旁白/主播/导师)...

**Her 知性元气**:温暖亲密的年轻女声,声线带有明显的沙哑和气息感,像清晨刚醒来的烟嗓质感。声音柔软但有厚度,带着慵懒的性感。像她贴着你的耳朵轻声说话,每个字都带着轻微的呼吸声。灵感来自电影 *Her* 的 Samantha。

### 配置说明

BookBuddy 目前使用 **Mimo TTS** 作为后端引擎:

1. 去 [100t.xiaomimimo.com](https://100t.xiaomimimo.com/) 注册
2. 复制你的 API Key(`sk-` 开头)
3. 配置到环境变量:
   ```bash
   export MIMO_API_KEY="你的key"
   ```

Mimo TTS 提供免费额度,声音克隆和基础 TTS 都在同一个 API 里。未来会支持更多引擎(微软 TTS 等)。

### 它能做什么

```
一句话版:把 .txt / .md 文件变成有声书
--------

四个场景,一个工具:

1️⃣ 有声书(逐字朗读)
   # 用内置声音(Mimo / 微软TTS 提供多种预制音色,免费可用)
   python3 generate_audio.py 书.txt --clean

   # 克隆自己的声音(录 5 秒就够了)
   python3 generate_audio.py 书.txt --voice-clone --ref-audio 我的声音.mp3

   # 克隆其他人的声音⚠️(请确保你有使用权,见伦理承诺)
   python3 generate_audio.py 书.txt --voice-clone --ref-audio 参考音频.mp3

2️⃣ 学英语(用喜欢的声音练听力)
   # 英文文章 → 你喜欢的声音朗读 → 边听边看原文
   python3 generate_audio.py english_article.txt --clean
   python3 generate_audio.py english_article.txt --voice-clone --ref-audio 我的声音.mp3

3️⃣ AI代读播客(先总结再读)
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

# 2. 获取 API Key(免费额度)
#    去 https://100t.xiaomimimo.com/ 注册 → 复制你的 tp-xxx 开头的 Key
export MIMO_API_KEY="你的key"

# 3. 生成第一本有声书
python3 generate_audio.py 你的书.txt --clean
```

> 💡 **没有书?** 试试一键下载公版书:
> `python3 generate_audio.py --download 道德经 --clean`

> 💡 **想用自己的声音?** 录 5 秒音频:
> `python3 generate_audio.py 书.txt --voice-clone --ref-audio 我录的5秒.mp3`

> 💡 **声音可以选** - 内置几十种预制音色,可以克隆自己的,也可以设计你喜欢的声线(低沉、磁性、温柔...),全看你怎么用。

### 技术亮点

| 特性 | 为什么重要 |
|:----|:----------|
| **NFKC 清洗** | 修正 PDF/OCR 的乱码字,读出来不崩 |
| **智能分片 ≤100字** | 防止 TTS 长句读飘、吞音、电音 |
| **断点续传** | 中断了重跑,跳过已生成的,不白等 |
| **--download** | 搜公版书/Gutenberg,一键下载转有声书 |
| **声音克隆** | 用 5 秒录音克隆任何声线(用户自备参考音频) |
| **分卷合并** | 每 30 段自动合并,ffmpeg 成最终 MP3 |

### 伦理承诺

> 此工具是**个人工具**,不是内容分发平台。
>
> - **声音**:请只使用你自己的声音,或你已获授权的声音参考
> - **内容**:请只朗读你有权访问的文本(你自己的文章、公版书、已购电子书)
> - **禁止**:不要用此工具生成的内容冒充他人,不要用于商业盈利
>
> 工具本身是中立的。你用它做什么,是你的选择。

---

## 🇺🇸 BookBuddy

### Have you had these moments?

- Bought a book and never opened it
- Felt reading was homework, not pleasure
- Stared at screens all day until your eyes hurt
- Wanted something good to listen to on your commute

### In the AI era, reading should be different

We live in an age of information overload, but the way we read hasn't changed in centuries - open a book, stare at the words, read one by one.

**In the AI era, reading should be more private, more personalized, more immersive, more friendly.**

- **More private**: Your book, your voice, your pace. No algorithm recommendations, no social pressure, just you and the text.
- **More personalized**: Read with the voice you love. Your own voice, a celebrity's voice, or any voice you want to listen to.
- **More immersive**: Close your eyes, let the voice carry you into the world of the text. Like someone sitting beside you, reading softly.
- **More friendly**: Eyes tired? Let your ears take over. No time? Listen during your commute. Can't focus? Try a different voice.

The barrier to reading is never the book itself. It's that first step of "starting to read." Turn reading into a listening experience, turn "I should read" into "I want to listen."

### Traditional Audiobooks vs AI Audiobooks

The biggest problem with traditional audiobooks: **you can only listen to the voice someone else chose.**

|  | Traditional Audiobooks | AI Audiobooks (BookBuddy) |
|:----|:----|:----|
| **Voice** | Fixed, you can't choose | You choose: your voice, a celebrity's voice, any voice you love |
| **Tone** | Fixed, you can't adjust | You adjust: speed, emotion, style, even add huskiness or breathiness |
| **Content** | Only bestsellers available | Any text: your notes, PDFs, web pages, papers |
| **Updates** | When the author records | Generate anytime, listen whenever |
| **Cost** | $20-30 per book | Free (Mimo offers free credits) |

**In the AI era, reading should be a highly personal experience.** Not "is there an audiobook for this book?" but "what voice do I want to read this book with?"

### Voice can be a companion

You might remember Samantha from the movie *Her* - an AI who used her voice to enter a man's life, reading with him, talking with him, thinking with him.

**BookBuddy's idea is simple: if you have a voice you love, reading with that voice makes you want to listen more - and finish more books.**

We can't build a full Samantha-like AI companion yet - an AI that truly understands you, responds to you, and lives with you. But we can start with voice, and use voice to create that sense of companionship.

**A voice that's always there, reading a book with you.** That's what BookBuddy does today - audiobooks.

The barrier to reading is never the book itself. It's that first step of "starting to read." Turn reading into a listening experience, turn "I should read" into "I want to listen."

- When your eyes are tired, let your ears take over
- When you want something good during your commute or before bed, read differently
- If you have reading difficulties, switch to audio input
- If you're learning English, practice with a voice you love

### We can't build Samantha yet, but we can start with voice

> **Use existing AI technology to make reading a pleasure, an enjoyment, an immersion.**

Samantha isn't TTS. She's companionship. We can't build a full AI companion system yet - but we can start with voice, and get closer, step by step. A voice that's always there, reading a book with you. That's what BookBuddy does today.

### Three modes, three ways to get your voice

| Mode | How |
|:----|:----|
| **🎤 Built-in voices** | Use directly, zero setup |
| **🎨 Voice design** | Describe the voice you want → `--voice-design "deep, magnetic male voice"` |
| **📝 Voice clone** | Record 5s → `--voice-clone --ref-audio` |

**Built-in voices (Mimo TTS):** 冰糖 (CN female), 茉莉 (CN female), 苏打 (CN male), 白桦 (CN male), Mia (EN female), Chloe (EN female), Milo (EN male), Dean (EN male)

**Voice design examples:**
```bash
# Sleep hypnosis (built-in preset)
python3 generate_audio.py book.txt --voice-design "睡前催眠"

# Custom: deep, magnetic late-night radio voice
python3 generate_audio.py book.txt --voice-design "deep magnetic male voice, like a late-night radio host"

# Custom: bright, energetic voice for motivation
python3 generate_audio.py book.txt --voice-design "bright, energetic young voice"
```

### Setup

1. Sign up at [100t.xiaomimimo.com](https://100t.xiaomimimo.com/)
2. Get your API Key (starts with `sk-`)
3. Set environment variable:
   ```bash
   export MIMO_API_KEY="your-key"
   ```

Mimo TTS has free credits included. Voice cloning and basic TTS use the same API.

### What it does

```bash
# Read a book with built-in voices
python3 generate_audio.py my_book.txt --clean

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

CC BY-NC-SA 4.0 - Free for personal use, no commercial use.
