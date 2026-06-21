#!/bin/bash
# BookBuddy TTS - Curl Test Examples
# 测试各种 TTS 模式

set -e

# 配置
API_KEY="${MIMO_API_KEY:-sk-your-api-key-here}"
BASE_URL="https://api.xiaomimimo.com/v1"

echo "========================================"
echo "BookBuddy TTS - Test Examples"
echo "========================================"
echo ""

# 1. 基本 TTS
echo "📌 Test 1: Basic TTS (白桦)"
echo "----------------------------------------"
curl -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts",
    "messages": [
      {
        "role": "user",
        "content": "你好，这是《道德经》第一章：道可道，非常道。名可名，非常名。"
      }
    ],
    "voice": "白桦",
    "chunk_size": 300
  }' | jq '.'
echo ""

# 2. 基本 TTS (茉莉)
echo "📌 Test 2: Basic TTS (茉莉)"
echo "----------------------------------------"
curl -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts",
    "messages": [
      {
        "role": "user",
        "content": "晚安，愿你有个好梦。"
      }
    ],
    "voice": "茉莉"
  }' | jq '.'
echo ""

# 3. 声音设计 (温柔私语 - BookBuddy 灵魂声线 👑)
echo "📌 Test 3: Voice Design (温柔私语)"
echo "----------------------------------------"
curl -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts-voicedesign",
    "messages": [
      {
        "role": "user",
        "content": "闭上眼睛，深呼吸，让自己放松下来。"
      }
    ],
    "preset": "温柔私语"
  }' | jq '.'
echo ""

# 4. 声音设计 (知识讲述)
echo "📌 Test 4: Voice Design (知识讲述)"
echo "----------------------------------------"
curl -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-tts-voicedesign",
    "messages": [
      {
        "role": "user",
        "content": "今天我们来聊聊《人类简史》中的有趣观点。"
      }
    ],
    "preset": "知识讲述"
  }' | jq '.'
echo ""

# 5. 获取音色列表
echo "📌 Test 5: List Voices"
echo "----------------------------------------"
curl -X GET "${BASE_URL}/voices" \
  -H "Authorization: Bearer ${API_KEY}" | jq '.'
echo ""

# 6. 获取预设列表
echo "📌 Test 6: List Voice Presets"
echo "----------------------------------------"
curl -X GET "${BASE_URL}/voice-presets" \
  -H "Authorization: Bearer ${API_KEY}" | jq '.'
echo ""

# 7. 健康检查
echo "📌 Test 7: Health Check"
echo "----------------------------------------"
curl -X GET "${BASE_URL}/health" \
  -H "Authorization: Bearer ${API_KEY}" | jq '.'
echo ""

echo "========================================"
echo "✅ All tests completed!"
echo "========================================"