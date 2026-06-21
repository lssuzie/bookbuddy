#!/bin/bash
# BookBuddy 快速测试脚本
# 用法: ./test-bookbuddy.sh [预设名]

set -e

# 检查 API Key
if [ -z "$MIMO_API_KEY" ]; then
    echo "⚠️  MIMO_API_KEY 未设置，请设置环境变量："
    echo "   export MIMO_API_KEY='sk-xxx'"
    echo ""
    echo "从 https://platform.xiaomimimo.com/token-plan 获取 API Key"
    exit 1
fi

# 检查 ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg 未安装，请安装："
    echo "   brew install ffmpeg"
    exit 1
fi

# 测试目录
TEST_DIR="test_output"
mkdir -p "$TEST_DIR"

# 默认测试内容（道德经）
BOOK="--download 道德经"

# 预设列表
PRESETS=("温柔私语" "知识讲述" "故事演绎" "播客主持" "睡前陪伴" "冥想引导")
VOICES=("冰糖" "茉莉" "苏打" "白桦")

echo "🎧 BookBuddy 测试脚本"
echo "===================="
echo ""

# 如果指定了预设名，只测试那个
if [ -n "$1" ]; then
    PRESETS=("$1")
fi

# 测试声音设计预设
echo "📝 测试声音设计预设..."
for preset in "${PRESETS[@]}"; do
    echo "  测试: $preset"
    python3 scripts/generate_audio.py $BOOK \
        --voice-design "$preset" \
        -o "$TEST_DIR/test_${preset}.mp3" \
        --clean \
        --max-segments 5 || true
done

# 测试内置音色
echo ""
echo "🎤 测试内置音色..."
for voice in "${VOICES[@]}"; do
    echo "  测试: $voice"
    python3 scripts/generate_audio.py $BOOK \
        -v "$voice" \
        -o "$TEST_DIR/test_voice_${voice}.mp3" \
        --clean \
        --max-segments 5 || true
done

echo ""
echo "✅ 测试完成！"
echo "📁 输出目录: $TEST_DIR/"
echo ""
echo "试听命令:"
for f in "$TEST_DIR"/*.mp3; do
    echo "  ffplay $f"
done