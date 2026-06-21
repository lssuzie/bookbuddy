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

### 一个声音，做所有事

你可能记得电影 *Her* 里的 Samantha——一个 AI，用她的声音走进了男主的生活，陪他读书、聊天、思考。

**BookBuddy 的想法和 *Her* 一样：你找到一个喜欢的声音，它陪你做所有事。**

不是"读论文用一个声音，播客换一个"——而是像 Samantha 一样，一个声音一直陪着你。读论文、生成播客、教英语、睡前讲故事，都是同一个声音。

> **一个声音一直在你身边，陪你读一切。**

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

也可以直接把这段话发给支持 shell 的 AI Agent（Claude Code、Codex、Hermes 等）：

```text
帮我安装 BookBuddy skill。把 https://github.com/lssuzie/bookbuddy 克隆到 ~/.claude/skills/bookbuddy，安装后告诉我好了。
```

**装好后，BookBuddy 会主动问你：**

> **"你有自己喜欢的声音吗？"**

然后你可以说：
- "我喜欢林志玲的声音" → 调一个类似风格，用它读一切
- "用我的声音读道德经" → 克隆自己的声音
- "不知道，有什么推荐" → 试听温柔私语 👑

选好声音后，用它做所有事——读论文、播客、学英语、睡前，都是同一个声音，只是说话方式变了。

> 💡 如果你不关心选声音，直接说想听什么就行。BookBuddy 会按内容推荐合适的声音（比如"帮我读道德经"→知识讲述），不满意再说"换一个"。

---

### 听听效果

同一个声音（**温柔私语** 👑），三种场景：

| 场景 | 试听 |
|:-----|:-----|
| 🎙️ 播客（1.1x 自然聊天） | <audio src="samples/demo-podcast.mp3" controls></audio> |
| 📖 故事有声书（0.9x 有感情起伏） | <audio src="samples/demo-story.mp3" controls></audio> |
| 🧘 冥想引导（0.7x 空灵安宁） | <audio src="samples/demo-meditation.mp3" controls></audio> |

> 同一个声音，不同的读法。速度变了，风格变了，但声音还是那个声音。

---

### 三种找声音的方式

| 方式 | 怎么做 | 适合谁 |
|:-----|:------|:-------|
| **🎤 内置音色** | 直接用，零准备 | 想先试试的人 |
| **🎨 声音设计** | 描述你喜欢的风格 | 有偏好的声音风格，但没参考音频 |
| **📝 声音克隆** | 录 5 秒音频 | 想用自己的或朋友的声音 |

---

### 声音设计预设

| 名称 | 声线 |
|:-----|:-----|
| **温柔私语** 👑 | 温暖沙哑，贴耳私语 |
| **知识讲述** | 沉稳清晰，像老师在娓娓道来 |
| **故事演绎** | 有戏剧张力，能演绎情绪 |
| **播客主持** | 自然亲切，像朋友在聊天 |
| **睡前陪伴** | 温柔缓慢，越来越轻 |
| **冥想引导** | 空灵安宁，像从远处传来 |

先试 **温柔私语** 👑，不满意再换。

---

### 安装方式

**终端 AI 助手：**

```bash
npx skills add https://github.com/lssuzie/bookbuddy --skill bookbuddy
```

Claude Code、Codex、Hermes 等支持 shell 的 AI Agent 均可使用。

**图形界面平台：**

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
- 用喜欢的声音读一切
- 把文字变成有声书
- AI 代读 + 生成播客
- 克隆自己的声音陪伴阅读

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

灵感来自电影 *Her*。Samantha 不是 TTS，她是陪伴。一个声音一直在你身边，陪你读一切。

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

### One Voice, Everything

Remember Samantha from the movie *Her*? One voice that reads with you, talks with you, stays with you.

**BookBuddy works the same way: you find a voice you love, and it does everything with you.**

Not "use one voice for papers, another for podcasts" — one voice, always there. Reading papers, making podcasts, teaching English, bedtime stories. All with the same voice.

> **One voice, always with you, reading everything.**

---

### 30-Second Start

```bash
npx skills add https://github.com/lssuzie/bookbuddy --skill bookbuddy
```

Or tell your AI agent:

```text
Install the BookBuddy skill. Clone https://github.com/lssuzie/bookbuddy to ~/.claude/skills/bookbuddy.
```

**BookBuddy will ask you:**

> **"Do you have a voice you love?"**

Then say:
- "I like Taylor Swift's voice" → Agent creates a similar style
- "Use my voice to read this"
- "Not sure, what do you recommend?"
- "I want Gentle Whisper"

Find your voice and use it for everything — reading papers, podcasts, English, bedtime. Same voice, different delivery.

> 💡 Not interested in choosing a voice? Just say what you want to hear. BookBuddy will pick the right voice for your content (e.g., "read the Tao Te Ching" → Knowledge Narration). Say "switch" if you don't like it.

---

### Hear It in Action

Same voice (**Gentle Whisper** 👑), three scenarios:

| Scenario | Listen |
|:---------|:-------|
| 🎙️ Podcast (1.1x, conversational) | <audio src="samples/demo-podcast.mp3" controls></audio> |
| 📖 Storytelling (0.9x, emotional) | <audio src="samples/demo-story.mp3" controls></audio> |
| 🧘 Meditation (0.7x, ethereal) | <audio src="samples/demo-meditation.mp3" controls></audio> |

> Same voice, different delivery. Speed changes, style changes, but the voice stays the same.

---

### Three Ways to Find Your Voice

| Mode | How | Best For |
|:-----|:----|:---------|
| **🎤 Built-in Voices** | Use directly | Quick start |
| **🎨 Voice Design** | Describe your style | Have a preference, no audio reference |
| **📝 Voice Clone** | Record 5s audio | Your own voice or a friend's |

### Voice Design Presets

| Name | Voice |
|:-----|:------|
| **Gentle Whisper** 👑 | Warm, husky, intimate |
| **Knowledge Narration** | Steady, clear, authoritative |
| **Story Performance** | Dramatic, emotional range |
| **Podcast Host** | Natural, conversational |
| **Bedtime Companion** | Soft, slow, calming |
| **Meditation Guide** | Ethereal, peaceful |

Start with **Gentle Whisper** 👑. Switch anytime.

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

---

### Good For / Not Good For

**✅ Good for:**
- Read everything with your favorite voice
- Convert text to audiobooks
- AI reading + podcast generation
- Clone your own voice

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

Inspired by the movie *Her* — Samantha isn't TTS, she's companionship. One voice, always with you, reading everything.

---

<div align="center">

[Back to Top ↑](#-bookbuddy--ai读书伴侣) | [🇨🇳 中文](#-ai读书伴侣) | [GitHub](https://github.com/lssuzie/bookbuddy)

</div>