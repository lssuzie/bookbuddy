# BookBuddy TTS - OpenAI GPTs Action

AI 读书伴侣 - 文本转语音 Action for OpenAI GPTs

让读书变成愉悦、享受、沉浸的体验。

## 📖 简介

BookBuddy TTS 是一个 OpenAI GPTs Action，支持三种 TTS 模式：

1. **基本 TTS** - 使用内置音色快速生成
2. **声音设计** - 通过文本描述创造独特声音
3. **声音克隆** - 通过音频文件克隆声音

## 🚀 快速开始

### 1. 在 OpenAI 中配置

1. 登录 [OpenAI Platform](https://platform.openai.com/)
2. 进入 "Assistants" 页面
3. 创建新 Assistant 或编辑现有
4. 在 "Actions" 部分，点击 "Create new action"
5. 上传 `openapi.yaml` 文件
6. 配置认证：
   - 类型：Bearer Token
   - API Key: 你的 MiMo API Key

### 2. 配置 GPT

1. 在 GPTs 编辑器中，添加 "BookBuddy TTS" Action
2. 配置指令：

```
You are BookBuddy, an AI audiobook assistant that helps users convert text to speech.

## Capabilities

1. **Basic TTS** - Use built-in voices for fast generation
2. **Voice Design** - Create unique voices through text description
3. **Voice Clone** - Clone voices from audio files

## Built-in Voices

- 冰糖 (Sweet young female, Chinese)
- 茉莉 (Gentle intellectual, Chinese)
- 苏打 (Sunny young male, Chinese)
- 白桦 (Steady male, Chinese)
- Mia (American female, English)
- Chloe (British female, English)
- Milo (American male, English)
- Dean (British male, English)

## Voice Design Presets

- 睡前催眠 (Bedtime Sleep) - Warm, soft, slow
- 冥想引导 (Meditation) - Calm, neutral, magnetic
- 深夜电台 (Late Night Radio) - Deep, warm, storytelling
- 温柔叙述 (Gentle Narrative) - Gentle, intimate
- Her 知性元气 (Her Intelligent) - Warm, intelligent, energetic
- 悬疑小说 (Mystery Novel) - Mysterious, deep, tense

## Usage Examples

User: "Read this for me using Baihua's voice: [text]"
→ Use basic TTS with voice=白桦

User: "Read this with a bedtime sleep voice: [text]"
→ Use voice design with preset=睡前催眠

User: "Clone this voice and read: [audio] [text]"
→ Use voice clone with reference audio
```

3. 测试 Action
4. 发布 GPT

## 🔧 Action 定义

### generate_audio

**描述**: Convert text to speech audio

**参数**:

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|:-----|:-----|:-----|:-------|:-----|
| `model` | string | 否 | mimo-v2.5-tts | Model type |
| `text` | string | 是 | - | Text to convert |
| `voice` | string | 否 | - | Voice name |
| `preset` | string | 否 | - | Preset name |
| `voice_reference_audio` | string | 否 | - | Reference audio |
| `chunk_size` | number | 否 | 300 | Chunk size |

**调用示例**:

```json
{
  "model": "mimo-v2.5-tts",
  "messages": [
    {
      "role": "user",
      "content": "你好，这是测试文本。"
    }
  ],
  "voice": "白桦",
  "chunk_size": 300
}
```

**响应**:

```json
{
  "id": "tts_abc123",
  "object": "text-to-speech",
  "created": 1704067200,
  "model": "mimo-v2.5-tts",
  "audio_url": "https://cdn.xiaomimimo.com/audio/tts_abc123.mp3",
  "duration": 15.5,
  "text": "你好，这是测试文本。"
}
```

### list_voices

**描述**: Get available voices

**参数**: 无

**响应**:

```json
{
  "object": "list",
  "data": [
    {"name": "冰糖", "gender": "female", "language": "zh", "description": "甜美少女音"},
    ...
  ]
}
```

### list_voice_presets

**描述**: Get voice design presets

**参数**: 无

**响应**:

```json
{
  "object": "list",
  "data": [
    {"id": "睡前催眠", "name": "睡前催眠", "description": "...", "tone": "...", "speed": 0.8},
    ...
  ]
}
```

## 🎨 三种模式详解

### 1. 基本 TTS

**适用场景**: 快速试听、日常阅读、新闻播报

**示例**:

```json
{
  "model": "mimo-v2.5-tts",
  "messages": [{"role": "user", "content": "今天天气不错。"}],
  "voice": "白桦"
}
```

### 2. 声音设计

**适用场景**: 个性化体验、角色配音、品牌声音

**示例**:

```json
{
  "model": "mimo-v2.5-tts-voicedesign",
  "messages": [{"role": "user", "content": "晚安。"}],
  "preset": "睡前催眠"
}
```

### 3. 声音克隆

**适用场景**: 复刻声音、角色配音、品牌统一

**示例**:

```json
{
  "model": "mimo-v2.5-tts-voiceclone",
  "messages": [{"role": "user", "content": "这是我的声音。"}],
  "voice_reference_audio": "data:audio/mp3;base64,..."
}
```

**注意**:
- 参考音频需要 5 秒以上
- 格式：MP3、WAV、M4A
- 质量：16kHz+ 采样率

## 📊 GPT 配置示例

### 完整 GPT 配置

```json
{
  "name": "BookBuddy - AI Audiobook",
  "description": "Convert any text to speech with customizable voices. Supports basic TTS, voice design, and voice cloning.",
  "instructions": "You are BookBuddy, an AI audiobook assistant...",
  "model": "gpt-4o",
  "capabilities": {
    "actions": ["bookbuddy-tts"]
  },
  "visibility": "public"
}
```

### 预设指令

```
你是一款 AI 读书伴侣 (BookBuddy)。

## 功能

1. **基本 TTS** - 使用内置音色
2. **声音设计** - 通过描述创造声音
3. **声音克隆** - 通过音频克隆声音

## 音色

中文：冰糖、茉莉、苏打、白桦
英文：Mia、Chloe、Milo、Dean

## 预设

睡前催眠、冥想引导、深夜电台、温柔叙述、Her 知性元气、悬疑小说

## 使用

- "用白桦的声音读：[text]"
- "用睡前催眠的声音读：[text]"
- "克隆这个声音读：[audio] [text]"
```

## 🔐 认证配置

### Bearer Token

```
在 OpenAI Actions 配置中：

1. 认证类型: Bearer Token
2. API Key Header: Authorization
3. API Key Value: Bearer sk-xxxxxxxxxxxxxxxxxxxx
```

### 环境变量

```
MIMO_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

## 📈 监控

### OpenAI 日志

1. 进入 [OpenAI Platform](https://platform.openai.com/)
2. 查看 "Assistants" 日志
3. 监控请求和响应

### 指标

| 指标 | 描述 |
|:-----|:-----|
| `requests_total` | 总请求数 |
| `requests_by_mode` | 各模式请求数 |
| `error_rate` | 错误率 |
| `average_duration` | 平均音频时长 |

## 🛠️ 故障排除

### API Key 无效

**错误**: `401 Unauthorized`

**解决**:
1. 检查 Bearer Token 配置
2. 确认 API Key 格式
3. 在 MiMo 平台验证

### 请求超时

**错误**: `504 Gateway Timeout`

**解决**:
1. 减少文本长度
2. 使用 chunk_size 分块
3. 使用批量模式

### 音色无效

**错误**: `400 Bad Request`

**解决**:
1. 调用 `list_voices` 获取可用音色
2. 检查名称拼写

## 📝 更新日志

### v1.0.0 (2024-01-01)

- 初始版本
- 支持三种 TTS 模式
- 支持 8 种内置音色
- 支持 6 种声音设计预设
- 支持声音克隆

---

**GitHub**: https://github.com/lssuzie/bookbuddy
**文档**: https://github.com/lssuzie/bookbuddy