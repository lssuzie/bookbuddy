# 本地调试与预检指南

在启动大批量文本转语音（TTS）合成之前，请务必进行以下本地调试与依赖检查，避免因配置错误导致额度浪费或中途崩溃。

## 1. 依赖与环境预检

在终端运行以下命令，确保系统已安装必需的底层合并工具 `ffmpeg`：

```bash
ffmpeg -version
```

* **如果未安装**：
  * macOS: `brew install ffmpeg`
  * Windows: 下载 ffmpeg 官网二进制包并将其加入系统环境变量 `PATH`。

## 2. API 连通性快速测试

在终端运行以下极简命令（请替换为您的实际 `API_KEY`），验证您的 Token / 网关是否可达：

```bash
curl -X POST "https://token-plan-cn.xiaomimimo.com/v1/chat/completions" \
     -H "Authorization: Bearer tp-xxxx" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "mimo-v2.5-tts",
       "messages": [{"role": "user", "content": "你好"}],
       "audio": {"format": "mp3", "voice": "白桦"}
     }' --output test.mp3
```

* 检查是否成功生成 `test.mp3`。如果返回 JSON 报错（如 401），说明您的 API Key 或网关配置有误。

## 3. 音色与参数试听（Dry-run）

**严禁在未试听的情况下直接启动全书合成！**
* **调试方法**：
  1. 截取文本中具有代表性的一句话或一个段落（建议 80 字左右，包含停顿和感叹号）。
  2. 使用您的 TTS 脚本仅针对这单段文本运行一次合成。
  3. 仔细试听合成出来的音频：
     * **语速**是否合适？（太快或太慢可在 `speed` 中微调，或在客户端加速）。
     * **语气情感**是否符合预期？（如果不符合，调整 user messages 中的提示词描述，参考 [voice_clone.md](voice_clone.md) 或 [mimo_api.md](mimo_api.md)）。
     * **是否有电音/金属音**？如果出现，尝试替换 reference 种子音频。
