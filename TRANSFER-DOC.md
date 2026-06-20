# BookBuddy 项目交接文档

**创建时间**: 2025-06-21
**最后更新**: 2025-06-21
**项目状态**: 核心功能完成，待发布和文档完善

---

## 📌 项目定位

**BookBuddy (AI 读书伴侣)** — 把读书变成愉悦、享受、沉浸的体验。

**核心定位**:
- 主要定位：**Skill** — 被 AI Agent 调用
- 次要定位：独立 CLI 工具
- 未来可能：网页版

**灵感来源**: 电影 *Her* 中的 Samantha — 不是简单的 TTS，而是阅读陪伴。

---

## 🏗️ 项目结构

```
~/bookbuddy/                          # 主项目目录（Git 仓库）
├── SKILL.md                          # Skill 入口文档（Agent 使用指南）
├── README.md                         # 用户文档（CLI 使用指南）
├── scripts/
│   ├── generate_audio.py             # 核心脚本（3种模式）
│   └── test-bookbuddy.sh             # 快速测试脚本
├── references/
│   ├── skill-voice-guide.md          # 声音选择指南
│   ├── skill-cli-reference.md        # CLI 命令参考
│   ├── skill-troubleshooting.md      # 故障排除
│   ├── skill-voice-clone.md          # 声音克隆指南
│   └── mimo_api.md                   # Mimo API 参考
├── samples/                          # 示例文本
│   └── 道德经.txt
└── BOOKBUDDY-PRODUCT-THINKING.md     # 产品思考文档（本地，不推送到 GitHub）
```

**本地关联**:
- `.agents/skills/bookbuddy` → 软链接到 `~/bookbuddy/`
- `.agents/skills/tony-leung-tts` → 私有声音克隆参考（梁朝伟）
- `.agents/skills/tony-audiobook` → 私有编排 Skill

---

## ✅ 已完成功能

### 核心功能

| 功能 | 状态 | 说明 |
|:-----|:-----|:-----|
| **基本 TTS** | ✅ | `mimo-v2.5-tts`，8 个内置音色 |
| **声音设计** | ✅ | `mimo-v2.5-tts-voicedesign`，文本描述生成声音 |
| **声音克隆** | ✅ | `mimo-v2.5-tts-voiceclone`，5秒音频克隆 |
| **智能分块** | ✅ | 根据模式自动调整（clone ≤100, TTS ≤300, design ≤500） |
| **中文支持** | ✅ | 道德经测试成功（16分钟音频） |

### 声音预设

| 预设 | 风格 | 适用场景 |
|:-----|:-----|:-----|
| 睡前催眠 | 轻柔、缓慢 | 睡前读物、冥想 |
| 冥想引导 | 平静、空灵 | 冥想、正念 |
| 深夜电台 | 温暖、磁性 | 故事、散文 |
| 温柔叙述 | 亲切、柔和 | 儿童读物、情感类 |
| **Her 知性元气** | 温暖、沙哑、气息感 | 小说、一般阅读（推荐） |
| 悬疑小说 | 低沉、神秘 | 推理、惊悚 |

### 内置音色（8个）

| 中文名 | 语言 | 性别 |
|:-----|:-----|:-----|
| 冰糖 | 中文 | 女 |
| 茉莉 | 中文 | 女 |
| 苏打 | 中文 | 男 |
| 白桦 | 中文 | 男 |
| Mia | 英文 | 女 |
| Chloe | 英文 | 女 |
| Milo | 英文 | 男 |
| Dean | 英文 | 男 |

### 文档

| 文档 | 状态 |
|:-----|:-----|
| README.md | ✅ 完整 |
| SKILL.md | ⚠️ 需更新（分支 B 未实现） |
| references/voice-guide | ✅ |
| references/cli-reference | ✅ |
| references/troubleshooting | ✅ |
| references/voice-clone | ✅ |
| mimo_api.md | ✅ |

### GitHub

| 项目 | 状态 |
|:-----|:-----|
| 仓库名 | `lssuzie/bookbuddy` |
| 旧名 | `everything-to-podcast`（已重命名） |
| 推送 | ✅ 最新 commit `4a3995f` |
| Stars | 0（刚创建） |

---

## ⚠️ 已知问题

### SKILL.md 问题

1. **分支 B（播客）未实现** — 文档提到"AI 代读+播客"模式，但实际没有对应的脚本
2. **命令示例过时** — 仍使用 `-v 白桦` 等旧参数
3. **未提及声音设计** — 这是核心差异化功能，但 SKILL.md 没提到

### 其他

1. **Demo GIF** — 创建过但 PIL 字体渲染有问题，已移除
2. **错误处理** — API 错误提示不够友好
3. **进度显示** — 长音频生成时没有进度条

---

## 📋 待办事项（优先级排序）

### 🔴 高优先级

| # | 任务 | 原因 | 预估 |
|:--|:-----|:-----|:-----|
| 1 | **修复 SKILL.md** | 当前文档有未实现功能，会误导 Agent | 30 分钟 |
| 2 | **声音设计指南** | 这是差异化功能，但缺乏详细文档 | 1 小时 |
| 3 | **更多中文样本** | 只有道德经，不够代表性 | 1 小时 |

### 🟡 中优先级

| # | 任务 | 原因 | 预估 |
|:--|:-----|:-----|:-----|
| 4 | **进度条** | 长音频生成时看不到进度（用 `tqdm`） | 1 小时 |
| 5 | **错误处理优化** | API 错误提示不够友好 | 1 小时 |
| 6 | **教程文章** | "30秒克隆自己的声音做有声书" | 2 小时 |

### 🟢 低优先级

| # | 任务 | 原因 |
|:--|:-----|:-----|
| 7 | Demo GIF | Skill 不需要视觉演示 |
| 8 | 网页版 | 降低使用门槛（未来） |
| 9 | 批量处理 | 整本书一键生成 |

---

## 🚀 快速启动

### 环境要求

```bash
# 1. 安装依赖
pip install openai requests

# 2. 设置 API Key
export MIMO_API_KEY="sk-xxxxx"

# 3. 确保 ffmpeg 已安装
ffmpeg -version
```

### 获取 API Key

访问: https://100t.xiaomimimo.com/

### 测试

```bash
cd ~/bookbuddy
python3 scripts/test-bookbuddy.sh
```

### 生成有声书

```bash
# 使用内置音色
python3 scripts/generate_audio.py samples/道德经.txt -v 白桦

# 使用声音设计
python3 scripts/generate_audio.py samples/道德经.txt --voice-design "Her 知性元气"

# 克隆自己的声音
python3 scripts/generate_audio.py samples/道德经.txt --voice-clone --ref-audio my_voice.wav
```

---

## 🔐 敏感信息

| 项目 | 位置 | 说明 |
|:-----|:-----|:-----|
| 梁朝伟声音参考 | `.agents/skills/tony-leung-tts/` | **私有，不推送到 GitHub** |
| API Key | 环境变量 `MIMO_API_KEY` | 不要硬编码 |
| 产品思考文档 | `~/bookbuddy/BOOKBUDDY-PRODUCT-THINKING.md` | 本地，不推送到 GitHub |

---

## 📊 竞品分析

**结论**: 中文 + 声音克隆 + 完整有声书管道 = **完全空白**

| 竞品 | 中文 | 声音克隆 | 有声书 | 备注 |
|:-----|:-----|:-----|:-----|:-----|
| 剪映 TTS | ✅ | ❌ | ❌ | 短视频用 |
| Azure TTS | ✅ | ❌ | ❌ | 企业级 |
| 讯飞 | ✅ | ⚠️ | ✅ | 收费高 |
| **BookBuddy** | ✅ | ✅ | ✅ | **差异化** |

---

## 💡 产品愿景

> "把读书变成愉悦、享受、沉浸的体验"
> "让读书变成一件你想做的事，而不是你应该做的事"

**核心差异化**:
1. **声音设计** — 不只是克隆，而是创造
2. **Agent 优先** — 不是工具，是 Skill
3. **Her 灵感** — 陪伴感，不只是技术

---

## 📝 下次启动建议

1. **先修复 SKILL.md** — 删除分支 B，更新命令示例
2. **写声音设计指南** — 详细说明 6 个预设
3. **加进度条** — 用 `tqdm`
4. **发第一版** — 等待第一个 Star/Issue

---

**交接人**: SensenNova-v6.7-Flash (商量)
**接收人**: 下次会话的 AI 助手

**如果有任何疑问，查看**:
- `~/bookbuddy/README.md` — 用户文档
- `~/bookbuddy/SKILL.md` — Agent 使用指南
- `~/bookbuddy/BOOKBUDDY-PRODUCT-THINKING.md` — 产品思考（本地）
