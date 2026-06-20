# 🎧 BookBuddy · AI读书伴侣

> **AI读书伴侣 - 把读书变成愉悦、享受、沉浸的体验**

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/bookbuddy.svg?style=flat-square)](https://github.com/lssuzie/bookbuddy/stargazers)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](https://github.com/lssuzie/bookbuddy)

[中文](#-ai读书伴侣) | [English](#-bookbuddy)

---

## 📖 What is BookBuddy?

**BookBuddy is an AI audiobook companion** that transforms reading into a pleasurable, immersive experience. Inspired by the movie *Her*, it brings you a voice that's always there, reading with you.

把读书变成愉悦、享受、沉浸的体验。让读书变成一件你想做的事，而不是你应该做的事。

---

## ✨ Features

| Feature | Description |
|:--------|:------------|
| **3 TTS Modes** | Built-in voices, Voice Design, Voice Clone |
| **8 Built-in Voices** | 4 Chinese + 4 English voices |
| **6 Voice Presets** | Sleep, Meditation, Radio, Gentle, Her, Mystery |
| **Voice Cloning** | Clone any voice with 5s audio |
| **Smart Chunking** | Auto-adjusts for coherent speech |
| **Multi-platform** | CLI, Coze Plugin, Dify Tool, GPTs Action |

---

## 🎨 TTS Modes

| Mode | Description | Best For |
|:-----|:------------|:---------|
| **🎤 Built-in Voices** | Use directly, zero setup | Quick testing, daily reading |
| **🎨 Voice Design** | Describe the voice → create unique voice | Personalized experience, character voices |
| **📝 Voice Clone** | Record 5s audio → clone voice | Your own voice, voice you have rights to |

---

## 🎵 Built-in Voices

### Chinese Voices

| Voice | Gender | Style |
|:------|:-------|:------|
| 冰糖 | Female | Sweet, youthful |
| 茉莉 | Female | Gentle, intellectual |
| 苏打 | Male | Sunny, energetic |
| 白桦 | Male | Steady, magnetic |

### English Voices

| Voice | Gender | Style |
|:------|:-------|:------|
| Mia | Female | Bright American |
| Chloe | Female | Warm British |
| Milo | Male | Deep American |
| Dean | Male | Calm British |

---

## 🎭 Voice Design Presets

| Preset | Description | Use Case |
|:-------|:------------|:---------|
| **睡前催眠** | Warm, soft, slow | Bedtime stories |
| **冥想引导** | Calm, neutral, magnetic | Meditation audio |
| **深夜电台** | Deep, warm, storytelling | Radio shows |
| **温柔叙述** | Gentle, intimate | Novels |
| **Her 知性元气** | Warm, intelligent, energetic | Knowledge sharing |
| **悬疑小说** | Mysterious, deep, tense | Mystery novels |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- ffmpeg (for audio merging)
- Mimo API Key ([get free credits](https://100t.xiaomimimo.com/))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/lssuzie/bookbuddy.git
cd bookbuddy

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
export MIMO_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

### Generate Your First Audiobook

```bash
# Basic TTS with built-in voice
python scripts/generate_audio.py samples/道德经.txt --clean

# Voice clone (record 5s of your voice)
python scripts/generate_audio.py samples/道德经.txt --voice-clone --ref-audio my_voice.mp3

# Voice design (create custom voice)
python scripts/generate_audio.py samples/道德经.txt --voice-design "Her 知性元气"
```

---

## 📁 Project Structure

```
bookbuddy/
├── scripts/
│   ├── generate_audio.py    # Main TTS script
│   └── test-bookbuddy.sh    # Test all voice presets
├── samples/
│   └── 道德经.txt           # Sample text
├── references/
│   ├── skill-voice-guide.md       # Voice recommendations
│   ├── skill-cli-reference.md     # CLI documentation
│   ├── skill-voice-clone.md       # Voice cloning guide
│   └── skill-troubleshooting.md   # Troubleshooting
├── coze-plugin/           # Coze Plugin package
├── dify-plugin/           # Dify Plugin package
├── openai-action/         # OpenAI GPTs Action package
├── examples/
│   └── test-curl.sh       # API test examples
├── README.md
└── LICENSE
```

---

## 📖 Documentation

| Document | Description |
|:---------|:------------|
| [CLI Reference](references/skill-cli-reference.md) | Command-line usage guide |
| [Voice Guide](references/skill-voice-guide.md) | Voice selection recommendations |
| [Voice Clone Guide](references/skill-voice-clone.md) | How to clone voices |
| [Troubleshooting](references/skill-troubleshooting.md) | Common issues and solutions |

---

## 🔐 Configuration

### API Key Setup

1. Visit [100t.xiaomimimo.com](https://100t.xiaomimimo.com/)
2. Register and get your API Key (starts with `sk-`)
3. Set environment variable:

```bash
export MIMO_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

### ffmpeg Installation

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

| Feature | Why It Matters |
|:--------|:---------------|
| **NFKC Normalization** | Fixes OCR/PDF encoding issues |
| **Smart Chunking** | ≤100 chars for clone, ≤300 for TTS, ≤500 for design |
| **Resume Support** | Skip already-generated segments |
| **Auto Download** | Fetch public domain books automatically |
| **Batch Processing** | 30 segments → auto-merge to MP3 |

---

## 📚 Use Cases

| Scenario | Description |
|:---------|:------------|
| **Audiobooks** | Convert any text to audiobook |
| **Language Learning** | Practice listening with your favorite voice |
| **AI Reading Assistant** | Let AI read long articles for you |
| **Personalized Reading** | Read with the voice you love |

---

## ⚖️ Ethical Commitment

> This is a **personal tool**, not a content distribution platform.
>
> - **Voice**: Use only your own voice, or voices you have permission to use
> - **Content**: Read only text you have rights to access
> - **No**: Don't impersonate others, don't use for commercial purposes
>
> The tool is neutral. What you do with it is your choice.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

```bash
# Fork the repository
git clone https://github.com/lssuzie/bookbuddy.git

# Create a feature branch
git checkout -b feature/your-feature

# Commit and push
git commit -am 'Add new feature'
git push origin feature/your-feature

# Open a pull request
```

---

## 📄 License

CC BY-NC-SA 4.0 - Free for personal use, no commercial use.

---

## 🔗 Links

- **GitHub**: https://github.com/lssuzie/bookbuddy
- **Issues**: https://github.com/lssuzie/bookbuddy/issues
- **Mimo API**: https://100t.xiaomimimo.com/
- **Documentation**: https://github.com/lssuzie/bookbuddy/tree/main/references

---

## 🌟 About

**BookBuddy** - 让读书变成愉悦、享受、沉浸的体验。

> 一个声音一直在你身边，陪你读一本书。

Inspired by the movie *Her* - Samantha isn't TTS, she's companionship. We start with voice, and get closer, step by step.

---

## 🇺🇸 English Summary

**BookBuddy** is an AI audiobook companion that makes reading a pleasure, an enjoyment, an immersion.

- **3 TTS Modes**: Built-in voices, Voice Design, Voice Clone
- **8 Built-in Voices**: 4 Chinese + 4 English
- **6 Voice Presets**: Sleep, Meditation, Radio, Gentle, Her, Mystery
- **Voice Cloning**: Clone any voice with 5s audio
- **Multi-platform**: CLI, Coze, Dify, GPTs

**Get started**: Clone repo → Set API key → Generate audiobook

---

**BookBuddy** - A voice that's always there, reading a book with you.