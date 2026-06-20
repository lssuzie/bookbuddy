# 🎧 BookBuddy · AI读书伴侣

> **AI读书伴侣 - 把读书变成愉悦、享受、沉浸的体验**
>
> 让读书变成一件你想做的事,而不是你应该做的事。

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/bookbuddy.svg?style=flat-square)](https://github.com/lssuzie/bookbuddy/stargazers)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](https://github.com/lssuzie/bookbuddy)

[🇨🇳 中文](#-简介) | [🇺🇸 English](#-english-version)

---

## 📖 简介

**BookBuddy 是 AI 读书伴侣**，把读书变成愉悦、享受、沉浸的体验。灵感来自电影 *Her*，一个声音一直在你身边，陪你读一本书。

---

## ✨ 功能亮点

| 功能 | 说明 |
|:-----|:-----|
| **三种 TTS 模式** | 内置音色、声音设计、声音克隆 |
| **8 种内置音色** | 4 中文 + 4 英文 |
| **6 种声音设计预设** | 睡前催眠、冥想引导、深夜电台、温柔叙述、Her 知性元气、悬疑小说 |
| **声音克隆** | 5 秒音频即可克隆 |
| **智能分片** | 自动调整确保连贯 |
| **多平台支持** | CLI、Coze、Dify、GPTs |

---

## 🎨 三种模式

| 模式 | 怎么做 | 适合谁 |
|:-----|:------|:------|
| **🎤 内置音色** | 直接用，零准备 | 想先试试的人 |
| **🎨 声音设计** | 用文字描述创造声线 | 想要定制但没参考音频的人 |
| **📝 声音克隆** | 录 5 秒音频 | 想用自己的声音/有参考音频的人 |

---

## 🎵 内置音色

| 音色 | 语言 | 性别 | 感觉 |
|:-----|:-----|:-----|:-----|
| 冰糖 | 中文 | 女 | 清亮甜美 |
| 茉莉 | 中文 | 女 | 温柔知性 |
| 苏打 | 中文 | 男 | 清爽活力 |
| 白桦 | 中文 | 男 | 沉稳磁性 |
| Mia | 英文 | 女 | Bright |
| Chloe | 英文 | 女 | Warm |
| Milo | 英文 | 男 | Deep |
| Dean | 英文 | 男 | Calm |

---

## 🎭 声音设计预设

| 预设 | 描述 | 适用场景 |
|:-----|:-----|:---------|
| **睡前催眠** | 温暖、轻柔、缓慢 | 睡前故事 |
| **冥想引导** | 平静、中性、有磁性 | 冥想音频 |
| **深夜电台** | 低沉、温暖、有故事感 | 电台节目 |
| **温柔叙述** | 温柔、亲切 | 小说朗读 |
| **Her 知性元气** | 温暖、知性、有活力 | 知识分享 |
| **悬疑小说** | 神秘、低沉、有张力 | 悬疑推理 |

---

## 🚀 快速开始

### 前置条件

- Python 3.8+
- ffmpeg
- Mimo API Key ([获取免费额度](https://platform.xiaomimimo.com/token-plan))

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/lssuzie/bookbuddy.git
cd bookbuddy

# 2. 安装依赖
pip install -r requirements.txt

# 3. 设置 API Key
export MIMO_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

### 生成第一本有声书

```bash
# 基本 TTS
python scripts/generate_audio.py samples/道德经.txt --clean

# 声音克隆
python scripts/generate_audio.py samples/道德经.txt --voice-clone --ref-audio my_voice.mp3

# 声音设计
python scripts/generate_audio.py samples/道德经.txt --voice-design "Her 知性元气"
```

---

## 📁 项目结构

```
bookbuddy/
├── scripts/              # 源代码
│   ├── generate_audio.py # 主脚本
│   └── test-bookbuddy.sh # 测试脚本
├── references/           # 文档
│   ├── skill-cli-reference.md
│   ├── skill-voice-guide.md
│   ├── skill-voice-clone.md
│   └── skill-troubleshooting.md
├── samples/              # 示例
│   └── 道德经.txt
├── examples/             # 测试示例
│   └── test-curl.sh
├── coze-plugin/          # 部署指南
│   └── DEPLOY.md
├── README.md
└── SKILL.md
```

---

## 📖 文档

| 文档 | 说明 |
|:-----|:-----|
| [CLI 参考](references/skill-cli-reference.md) | 命令行使用指南 |
| [音色指南](references/skill-voice-guide.md) | 音色选择建议 |
| [声音克隆指南](references/skill-voice-clone.md) | 如何克隆声音 |
| [故障排除](references/skill-troubleshooting.md) | 常见问题解决 |

---

## 🔐 配置说明

BookBuddy 使用 **Mimo TTS** 作为后端引擎：

1. 去 [platform.xiaomimimo.com/token-plan](https://platform.xiaomimimo.com/token-plan) 注册
2. 获取 API Key（`sk-` 开头）
3. 配置到环境变量：
   ```bash
   export MIMO_API_KEY="你的key"
   ```

Mimo TTS 提供免费额度，声音克隆和基础 TTS 都在同一个 API 里。

### ffmpeg 安装

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# 从 https://ffmpeg.org/download.html 下载
```

---

## 📊 技术亮点

| 特性 | 说明 |
|:-----|:-----|
| **NFKC 清洗** | 修正 PDF/OCR 的乱码字 |
| **智能分片** | 防止 TTS 长句读飘、吞音 |
| **断点续传** | 中断了重跑，跳过已生成的 |
| **自动下载** | 搜公版书，一键下载转有声书 |
| **声音克隆** | 5 秒录音克隆任何声线 |
| **分卷合并** | 每 30 段自动合并为 MP3 |

---

## 📚 使用场景

| 场景 | 说明 |
|:-----|:-----|
| **有声书** | 把任何文本变成有声书 |
| **学英语** | 用喜欢的声音练听力 |
| **AI 代读** | 让 AI 帮你"听"完长文章 |
| **个性化阅读** | 用你喜欢的声音读书 |

---

## ⚖️ 伦理承诺

> 此工具是**个人工具**，不是内容分发平台。
>
> - **声音**：请只使用你自己的声音，或你已获授权的声音参考
> - **内容**：请只朗读你有权访问的文本
> - **禁止**：不要用此工具生成的内容冒充他人，不要用于商业盈利

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

```bash
git clone https://github.com/lssuzie/bookbuddy.git
git checkout -b feature/your-feature
git commit -am 'Add new feature'
git push origin feature/your-feature
```

---

## 📄 许可证

CC BY-NC-SA 4.0 - 个人免费，禁止商用。

---

## 🔗 链接

- **GitHub**: https://github.com/lssuzie/bookbuddy
- **Issues**: https://github.com/lssuzie/bookbuddy/issues
- **Mimo API**: https://platform.xiaomimimo.com/token-plan

---

## 🌟 关于

**BookBuddy** - 让读书变成愉悦、享受、沉浸的体验。

> 一个声音一直在你身边，陪你读一本书。

灵感来自电影 *Her* - Samantha 不是 TTS，她是陪伴。我们从声音开始，一步一步靠近。

---

<div align="center">

[回到顶部 ↑](#-bookbuddy--ai读书伴侣) | [🇨🇳 中文](#-简介) | [🇺🇸 English](#-english-version)

</div>

---

# 🇺🇸 English Version

## 📖 What is BookBuddy?

**BookBuddy is an AI audiobook companion** that transforms reading into a pleasurable, immersive experience. Inspired by the movie *Her*, it brings you a voice that's always there, reading with you.

---

## ✨ Features

| Feature | Description |
|:--------|:------------|
| **3 TTS Modes** | Built-in voices, Voice Design, Voice Clone |
| **8 Built-in Voices** | 4 Chinese + 4 English voices |
| **6 Voice Presets** | Sleep, Meditation, Radio, Gentle, Her, Mystery |
| **Voice Cloning** | Clone any voice with 5s audio |
| **Smart Chunking** | Auto-adjusts for coherent speech |
| **Multi-platform** | CLI, Coze, Dify, GPTs |

---

## 🎨 TTS Modes

| Mode | How | Best For |
|:-----|:----|:---------|
| **🎤 Built-in Voices** | Use directly | Quick testing |
| **🎨 Voice Design** | Describe the voice | Customized experience |
| **📝 Voice Clone** | Record 5s audio | Your own voice |

---

## 🎵 Built-in Voices

| Voice | Language | Gender | Style |
|:------|:---------|:-------|:------|
| 冰糖 | Chinese | Female | Sweet |
| 茉莉 | Chinese | Female | Gentle |
| 苏打 | Chinese | Male | Sunny |
| 白桦 | Chinese | Male | Steady |
| Mia | English | Female | Bright |
| Chloe | English | Female | Warm |
| Milo | English | Male | Deep |
| Dean | English | Male | Calm |

---

## 🎭 Voice Design Presets

| Preset | Description | Use Case |
|:-------|:------------|:---------|
| **睡前催眠** | Warm, soft, slow | Bedtime stories |
| **冥想引导** | Calm, neutral, magnetic | Meditation |
| **深夜电台** | Deep, warm, storytelling | Radio shows |
| **温柔叙述** | Gentle, intimate | Novels |
| **Her 知性元气** | Warm, intelligent, energetic | Knowledge sharing |
| **悬疑小说** | Mysterious, deep, tense | Mystery novels |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- ffmpeg
- Mimo API Key ([get free credits](https://platform.xiaomimimo.com/token-plan))

### Installation

```bash
git clone https://github.com/lssuzie/bookbuddy.git
cd bookbuddy
pip install -r requirements.txt
export MIMO_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

### Generate Your First Audiobook

```bash
# Basic TTS
python scripts/generate_audio.py samples/道德经.txt --clean

# Voice Clone
python scripts/generate_audio.py samples/道德经.txt --voice-clone --ref-audio my_voice.mp3

# Voice Design
python scripts/generate_audio.py samples/道德经.txt --voice-design "Her 知性元气"
```

---

## 📁 Project Structure

```
bookbuddy/
├── scripts/              # Source code
├── references/           # Documentation
├── samples/              # Sample texts
├── examples/             # Test examples
├── coze-plugin/          # Deployment guide
├── README.md
└── SKILL.md
```

---

## 📖 Documentation

| Document | Description |
|:---------|:------------|
| [CLI Reference](references/skill-cli-reference.md) | Command-line usage |
| [Voice Guide](references/skill-voice-guide.md) | Voice recommendations |
| [Voice Clone Guide](references/skill-voice-clone.md) | How to clone |
| [Troubleshooting](references/skill-troubleshooting.md) | Common issues |

---

## 🔐 Configuration

BookBuddy uses **Mimo TTS** as the backend engine:

1. Visit [platform.xiaomimimo.com/token-plan](https://platform.xiaomimimo.com/token-plan)
2. Get your API Key (starts with `sk-`)
3. Set environment variable:
   ```bash
   export MIMO_API_KEY="your-key"
   ```

Mimo TTS offers free credits. Voice cloning and basic TTS use the same API.

### Install ffmpeg

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

---

## 📊 Technical Highlights

| Feature | Description |
|:--------|:------------|
| **NFKC Normalization** | Fixes OCR/PDF encoding issues |
| **Smart Chunking** | Prevents speech errors |
| **Resume Support** | Skip already-generated segments |
| **Auto Download** | Fetch public domain books |
| **Voice Cloning** | Clone any voice with 5s audio |
| **Batch Processing** | Auto-merge to MP3 |

---

## 📚 Use Cases

| Scenario | Description |
|:---------|:------------|
| **Audiobooks** | Convert any text to audiobook |
| **Language Learning** | Practice listening |
| **AI Reading** | Let AI read long articles |
| **Personalized Reading** | Read with your favorite voice |

---

## ⚖️ Ethical Commitment

> This is a **personal tool**, not a content distribution platform.
>
> - **Voice**: Use only your own voice, or voices you have permission to use
> - **Content**: Read only text you have rights to access
> - **No**: Don't impersonate others, don't use for commercial purposes

---

## 🤝 Contributing

Contributions are welcome!

```bash
git clone https://github.com/lssuzie/bookbuddy.git
git checkout -b feature/your-feature
git commit -am 'Add new feature'
git push origin feature/your-feature
```

---

## 📄 License

CC BY-NC-SA 4.0 - Free for personal use, no commercial use.

---

## 🔗 Links

- **GitHub**: https://github.com/lssuzie/bookbuddy
- **Issues**: https://github.com/lssuzie/bookbuddy/issues
- **Mimo API**: https://platform.xiaomimimo.com/token-plan

---

## 🌟 About

**BookBuddy** - Make reading a pleasure, an enjoyment, an immersion.

> A voice that's always there, reading a book with you.

Inspired by the movie *Her* - Samantha isn't TTS, she's companionship. We start with voice, and get closer, step by step.

---

<div align="center">

[Back to Top ↑](#-bookbuddy--ai读书伴侣) | [🇨🇳 中文](#-简介) | [🇺🇸 English](#-english-version)

</div>