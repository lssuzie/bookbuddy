"""
BookBuddy TTS Plugin - Cloud Function
AI 读书伴侣 - 文本转语音插件

支持三种模式：
1. 基本 TTS - 使用内置音色
2. 声音设计 - 通过文本描述创造声音
3. 声音克隆 - 通过音频文件克隆声音
"""

import os
import json
import requests
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# 配置
MIMO_API_KEY = os.environ.get("MIMO_API_KEY")
MIMO_API_URL = "https://api.xiaomimimo.com/v1/chat/completions"
DEFAULT_CHUNK_SIZE = {
    "mimo-v2.5-tts": 300,
    "mimo-v2.5-tts-voicedesign": 500,
    "mimo-v2.5-tts-voiceclone": 100
}

# 内置音色列表
BUILTIN_VOICES = [
    {"name": "冰糖", "gender": "female", "language": "zh", "description": "甜美少女音"},
    {"name": "茉莉", "gender": "female", "language": "zh", "description": "温柔知性"},
    {"name": "苏打", "gender": "male", "language": "zh", "description": "阳光少年"},
    {"name": "白桦", "gender": "male", "language": "zh", "description": "沉稳男声"},
    {"name": "Mia", "gender": "female", "language": "en", "description": "American female"},
    {"name": "Chloe", "gender": "female", "language": "en", "description": "British female"},
    {"name": "Milo", "gender": "male", "language": "en", "description": "American male"},
    {"name": "Dean", "gender": "male", "language": "en", "description": "British male"}
]

# 声音设计预设
VOICE_DESIGN_PRESETS = {
    "睡前催眠": {
        "description": "温暖、轻柔、缓慢的女性声音，适合睡前阅读",
        "tone": "soft, warm, slow",
        "speed": 0.8
    },
    "冥想引导": {
        "description": "平静、中性、有磁性的声音，语速适中",
        "tone": "calm, neutral, magnetic",
        "speed": 0.9
    },
    "深夜电台": {
        "description": "低沉、温暖、有故事感的男声",
        "tone": "deep, warm, storytelling",
        "speed": 0.85
    },
    "温柔叙述": {
        "description": "温柔、亲切、适合小说朗读的女性声音",
        "tone": "gentle, intimate, narrative",
        "speed": 0.9
    },
    "Her 知性元气": {
        "description": "温暖、知性、有活力的女性声音，语速适中，适合睡前阅读。灵感来自《Her》中的 Samantha",
        "tone": "warm, intelligent, energetic, husky, breathy",
        "speed": 0.95
    },
    "悬疑小说": {
        "description": "神秘、低沉、有张力的声音，适合悬疑推理",
        "tone": "mysterious, deep, tense",
        "speed": 0.85
    }
}


def require_api_key(f):
    """验证 API Key"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "缺少有效的 Authorization header"}), 401
        
        token = auth_header.replace("Bearer ", "")
        if token != MIMO_API_KEY:
            return jsonify({"error": "无效的 API Key"}), 401
        
        return f(*args, **kwargs)
    return decorated


@app.route("/health", methods=["GET"])
def health_check():
    """健康检查"""
    return jsonify({"status": "healthy", "service": "bookbuddy-tts"})


@app.route("/v1/voices", methods=["GET"])
@require_api_key
def list_voices():
    """获取可用音色列表"""
    return jsonify({
        "object": "list",
        "data": BUILTIN_VOICES
    })


@app.route("/v1/voice-presets", methods=["GET"])
@require_api_key
def list_voice_presets():
    """获取声音设计预设列表"""
    return jsonify({
        "object": "list",
        "data": [
            {
                "id": preset_id,
                "name": preset_id,
                "description": preset_data["description"],
                "tone": preset_data["tone"],
                "speed": preset_data["speed"]
            }
            for preset_id, preset_data in VOICE_DESIGN_PRESETS.items()
        ]
    })


@app.route("/v1/tts/generate", methods=["POST"])
@require_api_key
def generate_audio():
    """
    生成音频
    
    支持三种模式：
    1. mimo-v2.5-tts - 基本 TTS
    2. mimo-v2.5-tts-voicedesign - 声音设计
    3. mimo-v2.5-tts-voiceclone - 声音克隆
    """
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "请求体不能为空"}), 400
        
        # 获取必要参数
        model = data.get("model", "mimo-v2.5-tts")
        text = data.get("text", "")
        
        if not text:
            return jsonify({"error": "text 参数不能为空"}), 400
        
        # 验证模型
        valid_models = [
            "mimo-v2.5-tts",
            "mimo-v2.5-tts-voicedesign",
            "mimo-v2.5-tts-voiceclone"
        ]
        if model not in valid_models:
            return jsonify({
                "error": f"无效的 model，可选值: {', '.join(valid_models)}"
            }), 400
        
        # 构建请求体
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ]
        }
        
        # 根据模式添加参数
        if model == "mimo-v2.5-tts":
            # 基本 TTS 模式
            voice = data.get("voice")
            if voice:
                # 验证音色名称
                voice_names = [v["name"] for v in BUILTIN_VOICES]
                if voice not in voice_names:
                    return jsonify({
                        "error": f"无效的 voice，可选值: {', '.join(voice_names)}"
                    }), 400
                payload["voice"] = voice
        
        elif model == "mimo-v2.5-tts-voicedesign":
            # 声音设计模式
            preset = data.get("preset")
            if preset:
                if preset not in VOICE_DESIGN_PRESETS:
                    return jsonify({
                        "error": f"无效的 preset，可选值: {', '.join(VOICE_DESIGN_PRESETS.keys())}"
                    }), 400
                payload["preset"] = preset
                # 添加预设的描述
                payload["voice_description"] = VOICE_DESIGN_PRESETS[preset]["description"]
        
        elif model == "mimo-v2.5-tts-voiceclone":
            # 声音克隆模式
            audio_data = data.get("voice_reference_audio")
            if not audio_data:
                return jsonify({
                    "error": "voice_reference_audio 参数不能为空（需要 5 秒以上的参考音频）"
                }), 400
            payload["voice_reference_audio"] = audio_data
        
        # 添加分块大小
        chunk_size = data.get("chunk_size", DEFAULT_CHUNK_SIZE.get(model, 300))
        payload["chunk_size"] = chunk_size
        
        # 调用 MiMo API
        headers = {
            "Authorization": f"Bearer {MIMO_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            MIMO_API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                "id": result.get("id", "tts_" + os.urandom(8).hex()),
                "object": "text-to-speech",
                "created": result.get("created", int(os.time())),
                "model": model,
                "audio_url": result.get("audio_url"),
                "audio_base64": result.get("audio_base64"),
                "duration": result.get("duration"),
                "text": text,
                "chunk_size": chunk_size
            })
        else:
            return jsonify({
                "error": f"MiMo API 调用失败: {response.status_code}",
                "details": response.text
            }), response.status_code
    
    except requests.exceptions.Timeout:
        return jsonify({"error": "请求超时，请检查文本长度或重试"}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"网络错误: {str(e)}"}), 503
    except Exception as e:
        return jsonify({"error": f"服务器错误: {str(e)}"}), 500


@app.route("/v1/tts/generate/batch", methods=["POST"])
@require_api_key
def generate_audio_batch():
    """
    批量生成音频
    
    用于处理长文本，自动分块并合并
    """
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "请求体不能为空"}), 400
        
        model = data.get("model", "mimo-v2.5-tts")
        text = data.get("text", "")
        
        if not text:
            return jsonify({"error": "text 参数不能为空"}), 400
        
        # 自动分块
        chunk_size = data.get("chunk_size", DEFAULT_CHUNK_SIZE.get(model, 300))
        chunks = []
        current_chunk = ""
        
        # 按句子分块
        sentences = text.replace("。", "。\n").replace("！", "！\n").replace("？", "？\n").split("\n")
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            if len(current_chunk) + len(sentence) <= chunk_size:
                current_chunk += sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = sentence
        
        if current_chunk:
            chunks.append(current_chunk)
        
        if not chunks:
            return jsonify({"error": "文本为空"}), 400
        
        # 并行生成音频
        audio_urls = []
        errors = []
        
        for i, chunk in enumerate(chunks):
            try:
                payload = {
                    "model": model,
                    "messages": [{"role": "user", "content": chunk}]
                }
                
                # 添加可选参数
                if data.get("voice"):
                    payload["voice"] = data["voice"]
                if data.get("preset"):
                    payload["preset"] = data["preset"]
                if data.get("voice_reference_audio"):
                    payload["voice_reference_audio"] = data["voice_reference_audio"]
                
                headers = {
                    "Authorization": f"Bearer {MIMO_API_KEY}",
                    "Content-Type": "application/json"
                }
                
                response = requests.post(
                    MIMO_API_URL,
                    headers=headers,
                    json=payload,
                    timeout=120
                )
                
                if response.status_code == 200:
                    result = response.json()
                    audio_urls.append({
                        "chunk_index": i,
                        "text": chunk,
                        "audio_url": result.get("audio_url"),
                        "duration": result.get("duration")
                    })
                else:
                    errors.append({
                        "chunk_index": i,
                        "error": response.text
                    })
            
            except Exception as e:
                errors.append({
                    "chunk_index": i,
                    "error": str(e)
                })
        
        # 返回结果
        return jsonify({
            "id": "tts_batch_" + os.urandom(8).hex(),
            "object": "text-to-speech-batch",
            "model": model,
            "total_chunks": len(chunks),
            "successful_chunks": len(audio_urls),
            "failed_chunks": len(errors),
            "audio_urls": audio_urls,
            "errors": errors,
            "total_duration": sum(
                item.get("duration", 0) for item in audio_urls
            )
        })
    
    except Exception as e:
        return jsonify({"error": f"服务器错误: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)