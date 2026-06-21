# BookBuddy TTS Plugin

AI 读书伴侣 - 文本转语音插件

让读书变成愉悦、享受、沉浸的体验。

## 📖 简介

BookBuddy TTS Plugin 是一个基于 MiMo API 的文本转语音插件，支持三种模式：

1. **基本 TTS** - 使用内置音色快速生成
2. **声音设计** - 通过文本描述创造独特声音
3. **声音克隆** - 通过音频文件克隆声音

## 🚀 快速开始

### 1. 部署到 Coze

1. 登录 [Coze 开发者平台](https://www.coze.com/open/plugin)
2. 点击 "创建 Plugin"
3. 选择 "OpenAPI Schema" 导入方式
4. 上传 `openapi.yaml` 文件
5. 配置 API Key（在环境变量中设置 `MIMO_API_KEY`）

### 2. 配置云端函数

1. 在 Plugin 配置页面，选择 "云端函数" 部署方式
2. 上传 `main.py` 和 `requirements.txt`
3. 设置环境变量：
   ```
   MIMO_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
   ```
4. 部署函数

### 3. 创建 Bot

1. 在 Coze 控制台创建新的 Bot
2. 添加 "BookBuddy TTS" Plugin
3. 配置 Bot 指令和预设参数

## 🔧 API 文档

### 基础信息

- **Base URL**: `https://api.coze.com/v1`
- **认证方式**: Bearer Token（在 Header 中）
- **数据格式**: JSON

### 接口列表

| 接口 | 方法 | 描述 |
|:-----|:-----|:-----|
| `/v1/tts/generate` | POST | 生成音频 |
| `/v1/tts/generate/batch` | POST | 批量生成音频 |
| `/v1/voices` | GET | 获取音色列表 |
| `/v1/voice-presets` | GET | 获取声音设计预设 |
| `/health` | GET | 健康检查 |

### 生成音频

**请求示例**：

```bash
curl -X POST "https://api.coze.com/v1/tts/generate" \
  -H "Authorization: Bearer {your_api_key}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts",
    "text": "你好，这是测试文本。",
    "voice": "白桦",
    "chunk_size": 300
  }'
```

**参数说明**：

| 参数 | 类型 | 必填 | 描述 |
|:-----|:-----|:-----|:-----|
| `model` | string | 否 | 模型名称，默认 `mimo-v2.5-tts` |
| `text` | string | 是 | 要转换的文本 |
| `voice` | string | 否 | 音色名称（基本 TTS 模式） |
| `preset` | string | 否 | 预设名称（声音设计模式） |
| `voice_reference_audio` | string | 否 | 参考音频（声音克隆模式） |
| `chunk_size` | integer | 否 | 分块大小，默认 300 |

**响应示例**：

```json
{
  "id": "tts_abc123",
  "object": "text-to-speech",
  "created": 1704067200,
  "model": "mimo-v2.5-tts",
  "audio_url": "https://cdn.xiaomimimo.com/audio/tts_abc123.mp3",
  "duration": 15.5,
  "text": "你好，这是测试文本。",
  "chunk_size": 300
}
```

### 批量生成音频

**请求示例**：

```bash
curl -X POST "https://api.coze.com/v1/tts/generate/batch" \
  -H "Authorization: Bearer {your_api_key}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts",
    "text": "第一章...\n第二章...\n第三章...",
    "voice": "白桦"
  }'
```

**响应示例**：

```json
{
  "id": "tts_batch_xyz789",
  "object": "text-to-speech-batch",
  "model": "mimo-v2.5-tts",
  "total_chunks": 3,
  "successful_chunks": 3,
  "failed_chunks": 0,
  "audio_urls": [
    {"chunk_index": 0, "audio_url": "...", "duration": 10.2},
    {"chunk_index": 1, "audio_url": "...", "duration": 8.5},
    {"chunk_index": 2, "audio_url": "...", "duration": 12.1}
  ],
  "total_duration": 30.8
}
```

### 获取音色列表

**请求示例**：

```bash
curl -X GET "https://api.coze.com/v1/voices" \
  -H "Authorization: Bearer {your_api_key}"
```

**响应示例**：

```json
{
  "object": "list",
  "data": [
    {"name": "冰糖", "gender": "female", "language": "zh", "description": "甜美少女音"},
    {"name": "茉莉", "gender": "female", "language": "zh", "description": "温柔知性"},
    {"name": "苏打", "gender": "male", "language": "zh", "description": "阳光少年"},
    {"name": "白桦", "gender": "male", "language": "zh", "description": "沉稳男声"},
    {"name": "Mia", "gender": "female", "language": "en", "description": "American female"},
    {"name": "Chloe", "gender": "female", "language": "en", "description": "British female"},
    {"name": "Milo", "gender": "male", "language": "en", "description": "American male"},
    {"name": "Dean", "gender": "male", "language": "en", "description": "British male"}
  ]
}
```

### 获取声音设计预设

**请求示例**：

```bash
curl -X GET "https://api.coze.com/v1/voice-presets" \
  -H "Authorization: Bearer {your_api_key}"
```

**响应示例**：

```json
{
  "object": "list",
  "data": [
    {
      "id": "睡前陪伴",
      "name": "睡前陪伴",
      "description": "温暖、轻柔、缓慢的女性声音，适合睡前阅读",
      "tone": "soft, warm, slow",
      "speed": 0.8
    },
    {
      "id": "温柔私语",
      "name": "温柔私语",
      "description": "温暖、知性、有活力的女性声音，灵感来自《Her》中的 Samantha",
      "tone": "warm, intelligent, energetic, husky, breathy",
      "speed": 0.95
    }
  ]
}
```

## 🎨 三种模式详解

### 1. 基本 TTS

使用内置音色快速生成音频。

**适用场景**：
- 快速试听
- 日常阅读
- 新闻播报

**示例**：

```json
{
  "model": "mimo-v2.5-tts",
  "text": "今天天气不错，适合读书。",
  "voice": "白桦"
}
```

### 2. 声音设计

通过文本描述创造独特的声音。

**适用场景**：
- 个性化阅读体验
- 角色配音
- 品牌声音

**示例**：

```json
{
  "model": "mimo-v2.5-tts-voicedesign",
  "text": "晚安，愿你有个好梦。",
  "preset": "睡前陪伴"
}
```

**预设列表**：

| 预设名称 | 描述 | 适用场景 |
|:---------|:-----|:---------|
| 温柔私语 👑 | 温暖沙哑，贴耳私语 | 一切——BookBuddy 灵魂声线 |
| 知识讲述 | 沉稳清晰，像老师在娓娓道来 | 知识阅读 |
| 故事演绎 | 有戏剧张力，能演绎情绪 | 小说故事 |
| 播客主持 | 自然亲切，像朋友在聊天 | 播客 |
| 睡前陪伴 | 温柔缓慢，越来越轻 | 睡前 |
| 冥想引导 | 空灵安宁，像从远处传来 | 冥想 |

### 3. 声音克隆

通过音频文件克隆声音。

**适用场景**：
- 复刻自己的声音
- 特定角色配音
- 品牌声音统一

**示例**：

```json
{
  "model": "mimo-v2.5-tts-voiceclone",
  "text": "这是我的克隆声音。",
  "voice_reference_audio": "data:audio/mp3;base64,..."
}
```

**注意**：
- 参考音频需要 5 秒以上
- 音频格式：MP3、WAV、M4A
- 音频质量：16kHz 以上采样率

## ⚠️ 错误处理

| 错误码 | 描述 | 解决方案 |
|:-------|:-----|:---------|
| 400 | 请求参数错误 | 检查参数格式和必填项 |
| 401 | 认证失败 | 检查 API Key 是否正确 |
| 404 | 资源不存在 | 检查接口路径 |
| 429 | 请求过于频繁 | 降低请求频率 |
| 500 | 服务器错误 | 稍后重试 |
| 503 | 服务不可用 | 检查服务状态 |
| 504 | 请求超时 | 检查文本长度或重试 |

## 🔐 安全建议

1. **保护 API Key**：不要在客户端代码中暴露 API Key
2. **使用环境变量**：通过环境变量管理敏感信息
3. **限制请求频率**：实现速率限制防止滥用
4. **验证输入**：对所有输入进行验证和清理
5. **HTTPS**：始终使用 HTTPS 传输数据

## 📊 监控和日志

### 健康检查

```bash
curl -X GET "https://api.coze.com/health" \
  -H "Authorization: Bearer {your_api_key}"
```

响应：

```json
{
  "status": "healthy",
  "service": "bookbuddy-tts"
}
```

### 日志格式

```
[2024-01-01 12:00:00] INFO 请求开始 model=mimo-v2.5-tts text_length=100
[2024-01-01 12:00:01] INFO 请求完成 duration=1.2s audio_url=https://...
[2024-01-01 12:00:02] ERROR 请求失败 error="timeout"
```

## 📝 开发计划

- [ ] 支持更多 TTS 引擎
- [ ] 音频格式转换（MP3 → WAV, OGG）
- [ ] 音频剪辑和合并
- [ ] 批量处理队列
- [ ] 用户自定义音色
- [ ] 多语言支持

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📞 联系方式

- GitHub: https://github.com/lssuzie/bookbuddy
- 文档: https://github.com/lssuzie/bookbuddy/blob/main/README.md

---

**BookBuddy** - 让读书变成愉悦、享受、沉浸的体验。