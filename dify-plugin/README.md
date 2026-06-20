# BookBuddy TTS - Dify Plugin

AI 读书伴侣 - 文本转语音插件 for Dify Platform

让读书变成愉悦、享受、沉浸的体验。

## 📖 简介

BookBuddy TTS 是一个 Dify 插件，支持三种 TTS 模式：

1. **基本 TTS** - 使用内置音色快速生成
2. **声音设计** - 通过文本描述创造独特声音
3. **声音克隆** - 通过音频文件克隆声音

## 🚀 快速开始

### 1. 在 Dify 中安装

1. 登录 [Dify 平台](https://cloud.dify.ai/)
2. 进入 "插件市场"
3. 搜索 "BookBuddy TTS"
4. 点击 "安装"

或者手动安装：

1. 下载插件包
2. 在 Dify 控制台点击 "添加插件"
3. 上传 `manifest.json` 和 `api.yaml`

### 2. 配置 API Key

1. 在 Dify 控制台，进入插件设置
2. 设置环境变量 `MIMO_API_KEY`
3. 获取 API Key：[MiMo API 平台](https://100t.xiaomimimo.com/)

### 3. 创建工作流

1. 创建新应用
2. 添加 "BookBuddy TTS" 工具
3. 配置参数：
   - `text`: 要转换的文本
   - `model`: 模型类型
   - `voice`: 音色（可选）
   - `preset`: 预设（可选）

## 🔧 工具列表

### generate_audio

**描述**: 将文本转换为音频

**参数**:

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|:-----|:-----|:-----|:-------|:-----|
| `model` | string | 否 | mimo-v2.5-tts | 模型类型 |
| `text` | string | 是 | - | 要转换的文本 |
| `voice` | string | 否 | - | 音色名称 |
| `preset` | string | 否 | - | 预设名称 |
| `voice_reference_audio` | file | 否 | - | 参考音频 |
| `chunk_size` | number | 否 | 300 | 分块大小 |

**使用示例**:

```yaml
# 基本 TTS
- tool: bookbuddy-tts/generate_audio
  parameters:
    model: mimo-v2.5-tts
    text: "你好，这是测试文本。"
    voice: 白桦

# 声音设计
- tool: bookbuddy-tts/generate_audio
  parameters:
    model: mimo-v2.5-tts-voicedesign
    text: "晚安，愿你有个好梦。"
    preset: 睡前催眠

# 声音克隆
- tool: bookbuddy-tts/generate_audio
  parameters:
    model: mimo-v2.5-tts-voiceclone
    text: "这是我的克隆声音。"
    voice_reference_audio: "{{uploaded_file}}"
```

### list_voices

**描述**: 获取可用音色列表

**参数**: 无

**响应**:

```json
{
  "object": "list",
  "data": [
    {"name": "冰糖", "gender": "female", "language": "zh", "description": "甜美少女音"},
    {"name": "茉莉", "gender": "female", "language": "zh", "description": "温柔知性"},
    ...
  ]
}
```

### list_voice_presets

**描述**: 获取声音设计预设列表

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

使用内置音色快速生成音频。

**适用场景**:
- 快速试听
- 日常阅读
- 新闻播报

**示例**:

```yaml
model: mimo-v2.5-tts
text: "今天天气不错，适合读书。"
voice: 白桦
```

### 2. 声音设计

通过文本描述创造独特的声音。

**适用场景**:
- 个性化阅读体验
- 角色配音
- 品牌声音

**示例**:

```yaml
model: mimo-v2.5-tts-voicedesign
text: "晚安，愿你有个好梦。"
preset: 睡前催眠
```

**预设列表**:

| 预设 | 描述 | 适用场景 |
|:-----|:-----|:---------|
| 睡前催眠 | 温暖、轻柔、缓慢 | 睡前故事 |
| 冥想引导 | 平静、中性、有磁性 | 冥想音频 |
| 深夜电台 | 低沉、温暖、有故事感 | 电台节目 |
| 温柔叙述 | 温柔、亲切 | 小说朗读 |
| Her 知性元气 | 温暖、知性、有活力 | 知识分享 |
| 悬疑小说 | 神秘、低沉、有张力 | 悬疑推理 |

### 3. 声音克隆

通过音频文件克隆声音。

**适用场景**:
- 复刻自己的声音
- 特定角色配音
- 品牌声音统一

**示例**:

```yaml
model: mimo-v2.5-tts-voiceclone
text: "这是我的克隆声音。"
voice_reference_audio: "{{uploaded_file}}"
```

**注意**:
- 参考音频需要 5 秒以上
- 音频格式：MP3、WAV、M4A
- 音频质量：16kHz 以上采样率

## 📊 工作流示例

### 简单文本转音频

```yaml
workflow:
  - start:
      variables:
        - name: text
          type: string
          required: true

  - bookbuddy_tts:
      tool: generate_audio
      parameters:
        model: mimo-v2.5-tts
        text: "{{text}}"
        voice: 白桦

  - answer:
      text: "音频已生成！\n\n时长：{{bookbuddy_tts.duration}} 秒\n链接：{{bookbuddy_tts.audio_url}}"
```

### 多模式选择

```yaml
workflow:
  - start:
      variables:
        - name: text
          type: string
          required: true
        - name: mode
          type: string
          enum: [tts, voicedesign, voiceclone]

  - choice:
      condition: "{{mode}} == 'tts'"
      next: tts_mode

  - choice:
      condition: "{{mode}} == 'voicedesign'"
      next: voicedesign_mode

  - tts_mode:
      tool: generate_audio
      parameters:
        model: mimo-v2.5-tts
        text: "{{text}}"
        voice: "{{voice}}"

  - voicedesign_mode:
      tool: generate_audio
      parameters:
        model: mimo-v2.5-tts-voicedesign
        text: "{{text}}"
        preset: "{{preset}}"

  - answer:
      text: "音频已生成！\n\n{{bookbuddy_tts.audio_url}}"
```

## 🔐 安全建议

1. **保护 API Key**: 不要在客户端暴露 API Key
2. **使用环境变量**: 通过 Dify 环境变量管理
3. **限制请求频率**: 配置速率限制
4. **验证输入**: 对所有输入进行验证

## 📈 监控

### 查看日志

1. 在 Dify 控制台，进入应用页面
2. 点击 "日志" 标签
3. 查看执行记录

### 监控指标

| 指标 | 描述 |
|:-----|:-----|
| `requests_total` | 总请求数 |
| `requests_by_mode` | 各模式请求数 |
| `average_duration` | 平均音频时长 |
| `error_rate` | 错误率 |

## 🛠️ 故障排除

### 常见问题

#### API Key 无效

**错误**: `{"error": "无效的 API Key"}`

**解决**:
1. 检查 `MIMO_API_KEY` 环境变量
2. 确认 API Key 格式：`sk-xxxxxxxxxxxxxxxxxxxx`
3. 在 MiMo 平台验证

#### 请求超时

**错误**: `{"error": "请求超时"}`

**解决**:
1. 减少文本长度
2. 使用 `chunk_size` 分块
3. 使用批量模式

#### 音色无效

**错误**: `{"error": "无效的 voice"}`

**解决**:
1. 使用 `list_voices` 获取可用音色
2. 检查音色名称拼写

## 📝 更新日志

### v1.0.0 (2024-01-01)

- 初始版本
- 支持三种 TTS 模式
- 支持 8 种内置音色
- 支持 6 种声音设计预设
- 支持声音克隆

---

**GitHub**: https://github.com/lssuzie/bookbuddy
**文档**: https://github.com/lssuzie/bookbuddy/blob/main/README.md