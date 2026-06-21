---
name: bookbuddy
description: "AI 读书伴侣 Skill - 把文本转换为有声书。支持内置音色、声音设计、声音克隆、AI 代读播客。"
---

# BookBuddy · AI 读书伴侣 Skill

> **把读书变成愉悦、享受、沉浸的体验。**

## 使用方式

安装后，直接对 Agent 说：

- "帮我读这本书"
- "用睡前催眠的声音读这本小说"
- "克隆我的声音，帮我读这封信"
- "帮我总结这篇论文，生成一个播客"

Agent 会自动调用这个 Skill 完成。

---

## 三种模式

### 🎤 内置音色（零准备）
8 种内置音色，直接使用。

```bash
python3 <skill>/scripts/generate_audio.py <文件> --voice 白桦
```

### 🎨 声音设计（文字创造声音）
用文字描述创造独特声线。6 种预设 + 自定义。

```bash
python3 <skill>/scripts/generate_audio.py <文件> --voice-design "睡前催眠"
python3 <skill>/scripts/generate_audio.py <文件> --voice-design "温暖沙哑的女声，像清晨刚醒来的烟嗓"
```

### 📝 声音克隆（5 秒复刻）
录 5 秒参考音频，克隆任何声音。

```bash
python3 <skill>/scripts/generate_audio.py <文件> --voice-clone --ref-audio <音频>
```

---

## 使用场景

### 📚 有声书
用户说"帮我读这本书" → Agent 确认文件 → 调用 TTS → 返回音频

### 🎭 声音定制
用户说"用睡前催眠的声音读" → Agent 确认预设 → 调用 TTS → 返回音频

### 🎤 声音克隆
用户说"克隆我的声音" → Agent 引导录 5 秒 → 调用 TTS → 返回音频

### 🎙 AI 代读播客
用户说"帮我总结这本书生成播客" → Agent 阅读全文 → 口语化总结 → 调用 TTS → 返回播客

---

## 内置音色

| 中文 | 英文 |
|:-----|:-----|
| 冰糖（清亮甜美） | Mia（Bright） |
| 茉莉（温柔知性） | Chloe（Warm） |
| 苏打（清爽活力） | Milo（Deep） |
| 白桦（沉稳磁性） | Dean（Calm） |

## 声音设计预设

睡前催眠 | 冥想引导 | 深夜电台 | 温柔叙述 | **Her 知性元气** | 悬疑小说

---

## 参考文档

- [CLI 参考](references/skill-cli-reference.md)
- [音色指南](references/skill-voice-guide.md)
- [声音克隆指南](references/skill-voice-clone.md)
- [故障排除](references/skill-troubleshooting.md)

---

## 伦理承诺

> **声音**：只使用你自己的声音，或已获授权的声音参考
> **内容**：只朗读你有权访问的文本
> **禁止**：冒充他人、商业盈利

---

> [!WARNING]
> 本技能仅限个人学习、研究与技术交流使用，严禁用于任何商业用途。