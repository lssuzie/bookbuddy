# 🎧 BookBuddy · AI读书伴侣

> **AI读书伴侣 Skill - 把读书变成愉悦、享受、沉浸的体验**
>
> 一个支持三种 TTS 模式的 Skill/Plugin，可部署到 Coze、Dify、OpenAI GPTs 等平台

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/bookbuddy.svg?style=flat-square)](https://github.com/lssuzie/bookbuddy/stargazers)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](https://github.com/lssuzie/bookbuddy)

---

## 📦 这是什么？

**BookBuddy 是一个 Skill/Plugin**，让你的 AI Agent 具备文本转语音能力。

**支持平台**：Coze Plugin | Dify Tool | OpenAI GPTs Action

---

## 🎨 三种 TTS 模式

| 模式 | 说明 | 适用场景 |
|:-----|:-----|:---------|
| **基本 TTS** | 8 种内置音色，快速生成 | 日常阅读、新闻播报 |
| **声音设计** | 6 种预设 + 自定义描述 | 个性化体验、角色配音 |
| **声音克隆** | 5 秒音频克隆声音 | 复刻自己的声音 |

### 内置音色（8 种）

| 中文 | 英文 |
|:-----|:-----|
| 冰糖（甜美少女） | Mia（美式女声） |
| 茉莉（温柔知性） | Chloe（英式女声） |
| 苏打（阳光少年） | Milo（美式男声） |
| 白桦（沉稳男声） | Dean（英式男声） |

### 声音设计预设（6 种）

睡前催眠 | 冥想引导 | 深夜电台 | 温柔叙述 | **Her 知性元气** | 悬疑小说

> **Her 知性元气** - 温暖沙哑气息感女声，贴耳私语风格，灵感来自电影 *Her* 的 Samantha

---

## 🚀 快速部署

### Coze Plugin

```bash
# 1. 访问 https://www.coze.com/open/plugin
# 2. 创建 Plugin → 上传 coze-plugin/openapi.yaml
# 3. 配置环境变量 MIMO_API_KEY
# 4. 创建 Bot → 添加 BookBuddy TTS Plugin
```

### Dify Tool

```bash
# 1. 访问 https://cloud.dify.ai/
# 2. 插件市场 → 添加插件 → 上传 dify-plugin/manifest.json + api.yaml
# 3. 配置 MIMO_API_KEY
# 4. 创建工作流 → 添加 BookBuddy TTS 工具
```

### OpenAI GPTs Action

```bash
# 1. 访问 https://platform.openai.com/assistants
# 2. Actions → Create new action → 上传 openai-action/openapi.yaml
# 3. 配置 Bearer Token (MIMO_API_KEY)
# 4. 发布 GPT
```

---

## 💡 使用场景

| 场景 | 说明 |
|:-----|:-----|
| **AI 有声书** | 把任何文本变成有声书 |
| **英语学习** | 用喜欢的声音练听力 |
| **AI 代读** | 让 AI 帮你"听"完长文章 |
| **个性化阅读** | 用你喜欢的声音读书 |

---

## 📁 项目结构

```
bookbuddy/
├── coze-plugin/           # Coze Plugin (openapi.yaml + main.py)
├── dify-plugin/           # Dify Plugin (manifest.json + api.yaml)
├── openai-action/         # OpenAI GPTs Action (openapi.yaml)
├── scripts/               # CLI 工具 (generate_audio.py)
├── samples/               # 示例文本
├── references/            # 参考文档
├── examples/              # 测试脚本
└── README.md              # 本文档
```

---

## 🔐 配置

**必需**：
- [Mimo API Key](https://100t.xiaomimimo.com/) → `MIMO_API_KEY=sk-xxxxxxxxxxxx`

**可选**：
- ffmpeg：用于音频合并（CLI 模式）

---

## 📊 特性对比

| 特性 | BookBuddy | 其他 TTS Skill |
|:-----|:----------|:---------------|
| 多平台 | ✅ Coze/Dify/GPTs | 通常单平台 |
| 声音克隆 | ✅ 5 秒音频 | 部分支持 |
| 声音设计 | ✅ 文本描述 | 较少支持 |
| 中文优化 | ✅ 4 种音色 | 部分支持 |
| 开源 | ✅ 完整代码 | 部分闭源 |

---

## 📖 详细文档

- [CLI 使用指南](references/skill-cli-reference.md)
- [音色选择指南](references/skill-voice-guide.md)
- [声音克隆指南](references/skill-voice-clone.md)
- [故障排除](references/skill-troubleshooting.md)

---

## 🤝 贡献

```bash
git clone https://github.com/lssuzie/bookbuddy.git
cd bookbuddy
pip install -r coze-plugin/requirements.txt
export MIMO_API_KEY="sk-xxx"
./examples/test-curl.sh
```

---

## 📄 许可证

CC BY-NC-SA 4.0 - 个人免费，禁止商用。

---

## 📞 链接

- **GitHub**: https://github.com/lssuzie/bookbuddy
- **Issues**: https://github.com/lssuzie/bookbuddy/issues
- **Mimo API**: https://100t.xiaomimimo.com/

---

**BookBuddy** - 让读书变成愉悦、享受、沉浸的体验。

> 一个声音一直在你身边，陪你读一本书。