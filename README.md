# 🎧 BookBuddy · AI读书伴侣 Skill

> **AI 读书伴侣 Skill —— 把读书变成愉悦、享受、沉浸的体验。**
>
> 让读书变成一件你想做的事，而不是你应该做的事。

[![Skill](https://img.shields.io/badge/Skill-BookBuddy-FF4D6D?style=flat-square)](https://github.com/lssuzie/bookbuddy)
[![GitHub stars](https://img.shields.io/github/stars/lssuzie/bookbuddy?style=flat-square)](https://github.com/lssuzie/bookbuddy/stargazers)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](https://github.com/lssuzie/bookbuddy)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-6B5B95?style=flat-square)](https://github.com/lssuzie/bookbuddy)
[![Coze](https://img.shields.io/badge/Coze-Plugin-00B96B?style=flat-square)](https://github.com/lssuzie/bookbuddy)
[![Dify](https://img.shields.io/badge/Dify-Marketplace-1E3A5F?style=flat-square)](https://github.com/lssuzie/bookbuddy)

[🇨🇳 中文](#-ai读书伴侣) | [🇺🇸 English](#-english-version)

---

## 🇨🇳 AI读书伴侣

### 声音，可以是一种陪伴

你可能记得电影 *Her* 里的 Samantha——一个 AI，用她的声音走进了男主的生活，陪他读书、聊天、思考。

**BookBuddy 的想法很简单：如果你有一个喜欢的声音，用这个声音来读书，你会更愿意听，也更容易把一本书读完。**

Samantha 不是 TTS，她是陪伴。我们暂时还造不出一个像 Samantha 那样完整的 AI 伴侣——但我们可以从声音开始，一步一步靠近。

> **一个声音一直在你身边，陪你读一本书。这就是 BookBuddy 目前做到的。**

---

### 你也有过这些瞬间吗？

- 买了一本书，翻了两页就吃灰了
- 觉得读书是"应该做的事"，而不是"想做的事"
- 盯着屏幕一整天，眼睛真的快废了
- 通勤／做饭／睡前想听点东西，但播客质量太随机

**读书的障碍从来不是书本身，是"开始读"的那一步。**

---

### 30 秒开始

```bash
npx skills add https://github.com/lssuzie/bookbuddy --skill bookbuddy
```

也可以直接把这段话发给有 shell 权限的 AI Agent：

```text
帮我安装 BookBuddy skill。把 https://github.com/lssuzie/bookbuddy 克隆到 ~/.claude/skills/bookbuddy，安装后告诉我好了。
```

**装好后，BookBuddy 会主动问你：**

> **"你现在想听什么？"**

然后你可以说：
- "帮我读这本书"
- "我想听林志玲读一本书"
- "Karpathy 最近有什么新观点？帮我做成播客"
- "读个故事给我听"
- "睡前想听点东西"
- "用我的声音读这篇文字稿"
- "用我的声音读道德经"

Agent 会自动理解你的意图，选好声音，直接开读。

---

### 三种模式

| 模式 | 怎么做 | 适合谁 |
|:-----|:------|:-------|
| **🎤 内置音色** | 直接用，零准备 | 想先试试的人 |
| **🎨 声音设计** | 用文字描述创造声线 | 想要定制但没参考音频的人 |
| **📝 声音克隆** | 录 5 秒音频 | 想用自己的声音 |

---

### 场景 × 声音

**你在读什么？这里直接选：**

| 场景 | 推荐声音 | 为什么 |
|:-----|:---------|:-------|
| 📚 **知识阅读**（论文、教材、非虚构） | 「知识讲述」或 **白桦**（沉稳磁性） | 知识传递需要可信和清晰。知识讲述沉稳有权威感，像老师在娓娓道来 |
| 📖 **小说/网文**（文学、故事） | 「故事演绎」 | 小说需要戏剧张力和情绪演绎，故事演绎专为此设计 |
| 🎙️ **播客**（先总结再口语化输出） | 「播客主持」或 **苏打**（清爽活力） | 播客是内容输出，不是读书。播客主持像朋友在聊天 |
| 🗣️ **学英语** | **Mia**（美式）/ **Chloe**（英式） | 母语者是最安全的选择。也可以用声音设计描述你喜欢的声线风格，无侵权风险 |
| 😴 **睡前** | 「睡前陪伴」或 **冰糖**（清亮甜美） | 需要温柔缓慢的声音，越来越轻，像在哄睡 |
| 🧘 **冥想** | 「冥想引导」 | 空灵安宁，像从远处传来 |
| 🫂 **陪伴**（诗歌、信件、散文） | 「温柔私语」👑 | 不想学东西，只是想让一个声音陪着你 |

---

### 安装方式

**终端 AI 助手：**

```bash
npx skills add https://github.com/lssuzie/bookbuddy --skill bookbuddy
```

Claude Code、Codex、Hermes 等支持 shell 的 AI Agent 均可使用此命令安装。

或者在 Claude.ai 等图形界面平台：

| 平台 | 安装 |
|:-----|:-----|
| **Claude.ai** | 平台设置 → 上传 Skill 文件夹 |
| **Coze** | Bot 设置 → 添加 Plugin |
| **Dify** | 工作流 → 添加 Tool |
| **GPTs** | Assistant → Actions |

> 技术细节（API 配置、ffmpeg 安装、CLI 命令）见 [`references/`](./references/)。

---

### 适合 / 不适合

**✅ 合适：**
- 把 .txt / .md 变成有声书
- 用喜欢的声音朗读文章
- 克隆自己的声音陪伴阅读
- AI 代读 + 生成播客

**❌ 不合适：**
- 实时语音对话（不是语音助手）
- 长篇多人角色扮演（单角色 TTS）
- 商业音频分发（个人工具）

---

### 伦理承诺

> **声音**：只使用你自己的声音，或已获授权的声音参考
> **内容**：只朗读你有权访问的文本
> **禁止**：冒充他人、商业盈利

---

### 关于

灵感来自电影 *Her*。Samantha 不是 TTS，她是陪伴。我们从声音开始，一步一步靠近。

---

<div align="center">

[回到顶部 ↑](#-bookbuddy--ai读书伴侣) | [🇺🇸 English](#-english-version) | [GitHub](https://github.com/lssuzie/bookbuddy)

</div>

---

# 🇺🇸 English Version

## 🎧 BookBuddy · AI Audiobook Companion Skill

> **An AI reading companion — turn reading into a pleasure, not a chore.**

[![Skill](https://img.shields.io/badge/Skill-BookBuddy-FF4D6D?style=flat-square)](https://github.com/lssuzie/bookbuddy)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](https://github.com/lssuzie/bookbuddy)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-6B5B95?style=flat-square)](https://github.com/lssuzie/bookbuddy)

### Voice Can Be a Companion

Remember Samantha from the movie *Her*? An AI who used her voice to enter a man's life — reading with him, talking with him, thinking with him.

**BookBuddy's idea is simple: if you have a voice you love, reading with that voice makes you want to listen more — and finish more books.**

Samantha isn't TTS. She's companionship. We can't build a full AI companion yet — but we can start with voice.

> **A voice that's always there, reading a book with you. That's what BookBuddy does today.**

---

### 30-Second Start

```bash
npx skills add https://github.com/lssuzie/bookbuddy --skill bookbuddy
```

Or just tell your AI Agent:

```text
Install the BookBuddy skill. Clone https://github.com/lssuzie/bookbuddy to ~/.claude/skills/bookbuddy.
```

**Then just say:**
- "Read this book for me"
- "Use a bedtime story voice"
- "Clone my voice"
- "Summarize this article as a podcast"

---

### Three Modes

| Mode | How | Best For |
|:-----|:----|:---------|
| **🎤 Built-in Voices** | Use directly | Quick start |
| **🎨 Voice Design** | Describe the voice | Custom experience |
| **📝 Voice Clone** | Record 5s audio | Your own voice |

---

### Scenarios × Voices

**What are you reading? Pick your voice:**

| Scenario | Recommended Voice | Why |
|:---------|:-----------------|:----|
| 📚 **Knowledge** (non-fiction, papers) | **Knowledge Narration** or **白桦** (Steady) | Knowledge needs credibility. Steady and clear, like a teacher sharing insights |
| 📖 **Novels / Stories** | **Story Performance** | Novels need drama and emotion. Story Performance is built for this |
| 🎙️ **Podcast** (summary → conversation) | **Podcast Host** or **苏打** (Sunny) | Podcast is content delivery, not reading. Podcast Host sounds like a friend chatting |
| 🗣️ **Learn English** | **Mia** (US) / **Chloe** (UK) | Native speakers for authentic pronunciation |
| 😴 **Bedtime** | **Bedtime Companion** or **冰糖** (Sweet) | Soft and slow, gradually fading, like being gently lulled to sleep |
| 🧘 **Meditation** | **Meditation Guide** | Ethereal and peaceful, like a voice from afar |
| 🫂 **Companion** (poetry, letters, essays) | **Gentle Whisper** 👑 | Not for learning — just being accompanied by a voice |

---

### Installation

**Terminal AI assistants:**

```bash
npx skills add https://github.com/lssuzie/bookbuddy --skill bookbuddy
```

Works with Claude Code, Codex, Hermes, and any shell-capable AI agent.

**Graphical platforms:**

| Platform | How |
|:---------|:----|
| **Claude.ai** | Upload Skill folder |
| **Coze** | Add Plugin to Bot |
| **Dify** | Add Tool to Workflow |
| **GPTs** | Add Action to Assistant |

> Technical details (API setup, ffmpeg, CLI) → see [`references/`](./references/).

---

### Good For / Not Good For

**✅ Good for:**
- Convert .txt/.md to audiobooks
- Read with your favorite voice
- Clone your own voice
- AI reading + podcast generation

**❌ Not for:**
- Real-time voice chat
- Multi-character voice acting
- Commercial audio distribution

---

### Ethical Commitment

> **Voice**: Use only your own voice or authorized references
> **Content**: Read only text you have rights to
> **No**: Impersonation, commercial misuse

---

### About

Inspired by the movie *Her* — Samantha isn't TTS, she's companionship. We start with voice and get closer, step by step.

---

<div align="center">

[Back to Top ↑](#-bookbuddy--ai读书伴侣) | [🇨🇳 中文](#-ai读书伴侣) | [GitHub](https://github.com/lssuzie/bookbuddy)

</div>