# BookBuddy 交接文档

> 创建时间：2026-06-21
> 状态：开发中
> 下一步：平台商店提交

---

## 📖 项目概述

**BookBuddy** 是一个 AI 读书伴侣 Skill/Plugin，支持三种 TTS 模式：

| 模式 | 说明 | 适用场景 |
|:-----|:-----|:---------|
| **基本 TTS** | 8 种内置音色 | 日常阅读、新闻播报 |
| **声音设计** | 6 种预设 + 自定义描述 | 个性化体验、角色配音 |
| **声音克隆** | 5 秒音频克隆 | 复刻自己的声音 |

**产品愿景**：把读书变成愉悦、享受、沉浸的体验。灵感来自电影 *Her*。

**商业模式**：
- GitHub 开源（免费）→ 获客
- 平台商店订阅（收费）→ 变现

---

## 📊 当前状态

### ✅ 已完成

| 任务 | 状态 | 说明 |
|:-----|:-----|:-----|
| 核心代码开发 | ✅ 完成 | `scripts/generate_audio.py` |
| README 文档 | ✅ 完成 | 中英文双语，结构清晰 |
| SKILL.md | ✅ 完成 | Skill 定义 |
| 参考文档 | ✅ 完成 | 6 个参考文件 |
| 示例文本 | ✅ 完成 | `samples/道德经.txt` |
| 测试脚本 | ✅ 完成 | `examples/test-curl.sh` |
| Coze 部署指南 | ✅ 完成 | `coze-plugin/DEPLOY.md` |
| API 链接修复 | ✅ 完成 | `platform.xiaomimimo.com/token-plan` |

### ⏳ 待完成

| 任务 | 优先级 | 说明 |
|:-----|:-------|:-----|
| **Coze Store 提交** | 🔴 高 | 使用本地 `coze-plugin/` 文件 |
| **Dify Marketplace 提交** | 🔴 高 | 使用本地 `dify-plugin/` 文件 |
| **GPTs Store 提交** | 🟡 中 | 使用本地 `openai-action/` 文件 |
| 定价策略确定 | 🟡 中 | 免费层 + 专业层 + 企业层 |
| 服务部署 | 🟡 中 | 自己管理 API Key，提供托管 |

---

## 📁 项目结构

### GitHub 仓库（用户可见）

```
bookbuddy/
├── README.md                   # 项目文档（中英文）
├── SKILL.md                    # Skill 定义
├── .gitignore                  # 忽略配置
│
├── scripts/                    # 源代码
│   ├── generate_audio.py       # 主脚本
│   ├── test-bookbuddy.sh       # 测试脚本
│   └── extract_to_markdown.py  # 辅助脚本
│   └── merge_existing.py       # 音频合并
│   └── rename_volumes.py       # 分卷重命名
│
├── references/                 # 参考文档
│   ├── skill-cli-reference.md  # CLI 使用指南
│   ├── skill-voice-guide.md    # 音色选择指南
│   ├── skill-voice-clone.md    # 声音克隆指南
│   ├── skill-troubleshooting.md # 故障排除
│   ├── mimo_api.md             # Mimo API 规范
│   ├── voice-recommendations.md # 音色推荐
│   └── voice_clone.md          # 声音克隆参考
│
├── samples/                    # 示例
│   └── 道德经.txt              # 示例文本
│
├── examples/                   # 测试示例
│   └── test-curl.sh            # API 测试脚本
│
└── coze-plugin/                # Coze 部署指南
    ├── DEPLOY.md               # 部署到 Coze 的指南
    └── README.md               # API 文档
```

### 本地保留（不上传 GitHub）

| 文件/目录 | 用途 | 说明 |
|:----------|:-----|:-----|
| `BOOKBUDDY-PRODUCT-THINKING.md` | 本地开发笔记 | 产品思考、决策记录 |
| `TRANSFER-DOC.md` | 交接文档 | 本文档 |
| `dify-plugin/` | Dify 商店提交 | `manifest.json` + `api.yaml` |
| `openai-action/` | GPTs 商店提交 | `manifest.json` + `openapi.yaml` |
| `coze-plugin/openapi.yaml` | Coze 商店提交 | OpenAPI 3.0 定义 |
| `coze-plugin/main.py` | Coze 云端函数 | Flask 服务代码 |
| `coze-plugin/bot-config.json` | Coze Bot 配置 | 系统 prompt、greeting |
| `coze-plugin/requirements.txt` | Coze Python 依赖 | Flask 等 |
| `test_output/` | 测试输出 | 生成的音频文件 |

---

## 🔗 关键链接

| 链接 | 地址 | 说明 |
|:-----|:-----|:-----|
| **GitHub 仓库** | https://github.com/lssuzie/bookbuddy | 开源代码 |
| **GitHub Issues** | https://github.com/lssuzie/bookbuddy/issues | 问题反馈 |
| **Mimo API 注册** | https://platform.xiaomimimo.com/token-plan | 获取 API Key |
| **Mimo API 文档** | https://api.xiaomimimo.com/v1/chat/completions | API 端点 |

### 平台商店链接

| 平台 | 商店链接 | 提交入口 |
|:-----|:---------|:---------|
| **Coze** | https://www.coze.com/store | https://www.coze.com/open/plugin |
| **Dify** | https://marketplace.dify.ai | https://cloud.dify.ai/ |
| **OpenAI GPTs** | https://chat.openai.com/gpts | https://platform.openai.com/assistants |

---

## 🔐 配置信息

### API Key

- **前缀**：`sk-xxxxxxxxxxxxxxxxxxxx`
- **获取方式**：https://platform.xiaomimimo.com/token-plan
- **环境变量**：`export MIMO_API_KEY="sk-xxx"`

### Mimo TTS 模型

| 模型 | 用途 | 端点 |
|:-----|:-----|:-----|
| `mimo-v2.5-tts` | 基本 TTS | `https://api.xiaomimimo.com/v1/chat/completions` |
| `mimo-v2.5-tts-voicedesign` | 声音设计 | 同上 |
| `mimo-v2.5-tts-voiceclone` | 声音克隆 | 同上 |

### 内置音色

| 中文 | 英文 |
|:-----|:-----|
| 冰糖（甜美少女） | Mia（美式女声） |
| 茉莉（温柔知性） | Chloe（英式女声） |
| 苏打（阳光少年） | Milo（美式男声） |
| 白桦（沉稳男声） | Dean（英式男声） |

### 声音设计预设

| 预设 | 描述 |
|:-----|:-----|
| 睡前催眠 | 温暖、轻柔、缓慢 |
| 冥想引导 | 平静、中性、有磁性 |
| 深夜电台 | 低沉、温暖、有故事感 |
| 温柔叙述 | 温柔、亲切 |
| Her 知性元气 | 温暖、知性、有活力 |
| 悬疑小说 | 神秘、低沉、有张力 |

---

## 📋 下一步计划

### 1. Coze Store 提交（优先级：高）

**材料位置**：`~/bookbuddy/coze-plugin/`（本地）

**文件**：
- `openapi.yaml` - OpenAPI 3.0 定义
- `main.py` - Flask 云端函数
- `bot-config.json` - Bot 配置
- `requirements.txt` - Python 依赖

**步骤**：
```bash
1. 访问 https://www.coze.com/open/plugin
2. 创建 Plugin → 选择 "OpenAPI Schema"
3. 上传 coze-plugin/openapi.yaml
4. 配置环境变量 MIMO_API_KEY
5. 创建 Bot → 添加 "BookBuddy TTS" Plugin
6. 提交审核（1-3 天）
```

**定价建议**：
- 免费层：每月 5 次请求
- 专业层：¥19.9/月，无限次数
- 企业层：¥99/月，API 访问 + 定制

---

### 2. Dify Marketplace 提交（优先级：高）

**材料位置**：`~/bookbuddy/dify-plugin/`（本地）

**文件**：
- `manifest.json` - 插件声明
- `api.yaml` - OpenAPI 定义

**步骤**：
```bash
1. 访问 https://cloud.dify.ai/
2. 进入 "插件市场" → "添加插件"
3. 上传 dify-plugin/manifest.json + api.yaml
4. 配置 MIMO_API_KEY
5. 创建工作流 → 添加 "BookBuddy TTS" 工具
6. 提交审核（3-7 天）
```

**定价建议**：
- 免费层：每月 10 次请求
- 专业层：¥29.9/月，无限次数
- 企业层：¥199/月，私有部署

---

### 3. GPTs Store 提交（优先级：中）

**材料位置**：`~/bookbuddy/openai-action/`（本地）

**文件**：
- `manifest.json` - Action 声明
- `openapi.yaml` - OpenAPI 定义

**步骤**：
```bash
1. 访问 https://platform.openai.com/assistants
2. 创建/编辑 Assistant → "Actions" → "Create new action"
3. 上传 openai-action/openapi.yaml
4. 配置 Bearer Token (MIMO_API_KEY)
5. 发布 GPT
6. 提交审核（1-7 天）
```

**定价建议**：
- 免费层：每月 5 次请求
- 专业层：$4.99/月，无限次数
- 企业层：$49.99/月，API 访问

---

### 4. 服务部署（优先级：中）

**目标**：自己管理 API Key，提供托管服务

**选项**：
| 方案 | 说明 | 成本 |
|:-----|:-----|:-----|
| **Coze Cloud** | 使用 Coze 云端函数 | 免费额度 |
| **Dify Cloud** | 使用 Dify 云服务 | 免费额度 |
| **自建服务器** | VPS 部署 Flask | ¥50-200/月 |
| **Serverless** | AWS Lambda / Vercel | 按量付费 |

**建议**：先用 Coze/Dify 免费额度测试，用户量上来后再自建。

---

### 5. 定价策略（优先级：中）

**建议定价**：

| 层级 | Coze | Dify | GPTs |
|:-----|:-----|:-----|:-----|
| **免费** | 5 次/月 | 10 次/月 | 5 次/月 |
| **专业** | ¥19.9/月 | ¥29.9/月 | $4.99/月 |
| **企业** | ¥99/月 | ¥199/月 | $49.99/月 |

**考虑因素**：
- Mimo API 成本（免费额度 + 付费）
- 服务器成本
- 平台抽成（Coze/Dify 约 20-30%）
- 竞品价格

---

## 🛠️ 开发环境

### 本地开发

```bash
# 1. 克隆仓库
git clone https://github.com/lssuzie/bookbuddy.git
cd bookbuddy

# 2. 安装依赖
pip install -r requirements.txt  # 如果有
brew install ffmpeg              # macOS
sudo apt install ffmpeg          # Ubuntu

# 3. 配置 API Key
export MIMO_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"

# 4. 测试
./examples/test-curl.sh
python scripts/generate_audio.py samples/道德经.txt --clean
```

### 验证 API

```bash
curl -X POST "https://api.xiaomimimo.com/v1/chat/completions" \
  -H "Authorization: Bearer $MIMO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts",
    "messages": [{"role": "user", "content": "你好"}],
    "voice": "白桦"
  }'
```

---

## 📝 重要注意事项

### ⚠️ 版权风险

- **不要**使用名人声音（如梁朝伟）
- **只使用**自己的声音或已获授权的声音
- **不要**用于商业盈利（除非有授权）

### ⚠️ API 限制

- Mimo API 有免费额度限制
- 超过额度需要付费
- 监控使用量，避免意外扣费

### ⚠️ 平台审核

- Coze：1-3 天审核
- Dify：3-7 天审核
- GPTs：1-7 天审核
- 确保内容合规，避免被拒

---

## 📞 联系方式

- **GitHub**: https://github.com/lssuzie/bookbuddy
- **Issues**: https://github.com/lssuzie/bookbuddy/issues
- **Mimo API**: https://platform.xiaomimimo.com/token-plan

---

## 🌟 产品愿景

> **把读书变成愉悦、享受、沉浸的体验。**
>
> 让读书变成一件你想做的事，而不是你应该做的事。

灵感来自电影 *Her* - Samantha 不是 TTS，她是陪伴。我们从声音开始，一步一步靠近。

---

## ✅ 检查清单

### 提交前检查

- [ ] 所有文件已测试
- [ ] API Key 配置正确
- [ ] 文档完整无误
- [ ] 定价策略确定
- [ ] 服务部署方案确定

### 提交后检查

- [ ] 审核状态跟踪
- [ ] 用户反馈收集
- [ ] 使用量监控
- [ ] 收入统计
- [ ] 迭代计划制定

---

**交接完成！** 明天可以直接开始平台商店提交。

> 一个声音一直在你身边，陪你读一本书。