# Skill CLI 参考

> 供 Agent 调试或高级用户使用，常规场景不需要。

## 核心用法：先找声音，再用它读一切

```bash
# 1. 找到你的声音（三选一）
python3 generate_audio.py 书.txt -v 白桦                         # 内置音色
python3 generate_audio.py 书.txt --voice-design "温柔私语"       # 声音设计
python3 generate_audio.py 书.txt --voice-clone --ref-audio 参考.mp3 # 声音克隆

# 2. 同一个声音，不同演绎方式（调速度 + 调风格）
python3 generate_audio.py 论文.md --voice-design "温柔私语"           # 1.0x 正常速度
python3 generate_audio.py 故事.md --voice-design "温柔私语" -s 0.9    # 0.9x 慢一点，有感情
python3 generate_audio.py 播客.md --voice-design "温柔私语" -s 1.1    # 1.1x 快一点，像聊天
python3 generate_audio.py 睡前.md --voice-design "温柔私语" -s 0.7    # 0.7x 更慢，哄睡

# 3. 自定义演绎方式（声音不变，只变说话风格）
python3 generate_audio.py 书.md --voice-design "温柔私语" --design-prompt "用沉稳专业的语气朗读"
```

## 基本命令

```bash
# 最简单：一行命令生成有声书
python3 generate_audio.py 书.txt --clean

# 指定输出路径
python3 generate_audio.py 书.txt -o 输出路径.mp3

# 指定语速（1.0 = 正常，1.2 = 快，0.8 = 慢）
python3 generate_audio.py 书.txt -s 1.2
```

## 三种模式

### 1. 内置音色（预制）

```bash
python3 generate_audio.py 书.txt -v 白桦
python3 generate_audio.py 书.txt -v 茉莉
python3 generate_audio.py 书.txt -v 冰糖
python3 generate_audio.py 书.txt -v 苏打
```

### 2. 声音设计（文字描述）

```bash
# 使用内置预设
python3 generate_audio.py 书.txt --voice-design "温柔私语"
python3 generate_audio.py 书.txt --voice-design "睡前陪伴"
python3 generate_audio.py 书.txt --voice-design "故事演绎"

# 自定义描述
python3 generate_audio.py 书.txt --voice-design "低沉磁性的中年男声"
python3 generate_audio.py 书.txt --voice-design "元气明亮的少年音" \
  --design-prompt "用充满朝气的语气朗读，语速轻快"
```

### 3. 声音克隆（5 秒音频）

```bash
python3 generate_audio.py 书.txt --voice-clone --ref-audio 参考音频.mp3

# 指定克隆风格
python3 generate_audio.py 书.txt --voice-clone --ref-audio 参考.mp3 \
  --clone-prompt "标准流利普通话"
```

## 高级选项

```bash
# 文档清洗（去分隔线/URL/硬换行）
python3 generate_audio.py 书.txt --clean

# 保留分段文件（断点续传）
python3 generate_audio.py 书.txt --no-cleanup

# 指定 API Key（覆盖环境变量）
MIMO_API_KEY="sk-xxx" python3 generate_audio.py 书.txt

# 指定 chunk size（默认自动调整）
python3 generate_audio.py 书.txt --chunk-size 200

# 只下载不转音频
python3 generate_audio.py --download 道德经 --download-only
```

## 下载公版书

```bash
# 搜索并下载公版书
python3 generate_audio.py --download 道德经

# 下载后转有声书
python3 generate_audio.py --download 道德经 --clean

# 下载后用克隆声音朗读
python3 generate_audio.py --download "tao te ching" \
  --voice-clone --ref-audio 我的声音.mp3
```

## 环境变量

```bash
# API Key（必需）
export MIMO_API_KEY="sk-xxx"

# 从 .env 文件读取
python3 generate_audio.py --env ~/.gemini/antigravity/scratch/.env
```

## 依赖

```bash
# 必需
brew install ffmpeg

# 可选（PDF 支持）
pip3 install PyMuPDF
```

## 输出

- 音频文件：`<输出路径>.mp3`
- 分段文件：`<输出路径>_seg_001.mp3` 等（`--no-cleanup` 时保留）
- 日志：控制台输出进度