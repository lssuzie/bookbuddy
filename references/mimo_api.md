# MiMo TTS 请求规范与最佳实践

本参考文件适用于在 BookBuddy 中使用 MiMo TTS 模型进行高保真有声书音频合成时的配置与接口规范。

## 1. 接口配置

* **接口地址 (Base URL)**：`https://api.xiaomimimo.com/v1/chat/completions`
* **请求头**：`Authorization: Bearer sk-xxxx` (`sk-` 前缀 API Key)
* **模型代码**：`mimo-v2.5-tts`（基础 TTS）/ `mimo-v2.5-tts-voiceclone`（声音克隆）

## 2. 请求 Payload 示例

在调用 TTS 接口时，请发送以下 JSON 结构：

```json
{
  "model": "mimo-v2.5-tts",
  "messages": [
    {
      "role": "user",
      "content": "请用男声白桦朗读以下文字。注意：你的声音要磁性好听，同时请注入丰富且生动的感情，带有悬疑探案小说的叙事张力与情绪起伏，避免平淡无奇。请使用极其标准且规范的普通话，吐字要清晰有力、字字分明，避免任何含糊或吞音，不带口音。在句号等标点处，请保持清晰、较长且自然的停顿。"
    },
    {
      "role": "assistant",
      "content": "待朗读的规范化文本内容"
    }
  ],
  "audio": {
    "format": "mp3",
    "voice": "白桦",
    "speed": 1.0
  }
}
```

## 3. 合成建议

* 推荐在 TTS 端使用 `speed: 1.0` 生成。如需倍速，可在合并后的播放器端使用 WSOLA 算法进行无损本地加速，以维持最完美的原声音质。
