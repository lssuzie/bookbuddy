# Coze Plugin 部署指南

完整部署 BookBuddy TTS Plugin 到 Coze 平台的步骤。

## 📋 前置准备

### 1. 获取 MiMo API Key

1. 访问 [MiMo API 平台](https://100t.xiaomimimo.com/)
2. 注册/登录账号
3. 在 "API Key" 页面创建新的 API Key
4. 复制 API Key（格式：`sk-xxxxxxxxxxxxxxxxxxxx`）

### 2. 准备 Coze 账号

1. 访问 [Coze 平台](https://www.coze.com/)
2. 注册/登录账号
3. 进入 [开发者平台](https://www.coze.com/open/plugin)

## 🚀 部署步骤

### 第一步：创建 Plugin

1. 在 Coze 开发者平台，点击 "创建 Plugin"
2. 填写基本信息：

   | 字段 | 值 |
   |:-----|:---|
   | 名称 | BookBuddy TTS |
   | 描述 | AI 读书伴侣 - 文本转语音插件 |
   | Logo | 上传你的 Logo 图片 |
   | 文档链接 | https://github.com/lssuzie/bookbuddy |

3. 选择导入方式：
   - 选择 "OpenAPI Schema"
   - 上传 `openapi.yaml` 文件
   - 点击 "导入"

### 第二步：配置认证

1. 在 Plugin 配置页面，找到 "认证" 设置
2. 配置 API Key 认证：

   | 字段 | 值 |
   |:-----|:---|
   | 类型 | API Key |
   | 名称 | Authorization |
   | 位置 | Header |
   | 前缀 | Bearer |

3. 设置 API Key 值：
   - 点击 "添加环境变量"
   - 名称：`MIMO_API_KEY`
   - 值：`sk-xxxxxxxxxxxxxxxxxxxx`（你的 MiMo API Key）

### 第三步：配置云端函数

1. 在 Plugin 配置页面，找到 "云端函数" 设置
2. 选择部署方式：
   - 选择 "Python 3.9"
   - 选择 "上传文件"

3. 上传文件：
   - `main.py` - 主函数代码
   - `requirements.txt` - 依赖文件

4. 配置函数设置：

   | 字段 | 值 |
   |:-----|:---|
   | 函数名 | `main.handler` |
   | 内存 | 256MB |
   | 超时 | 60s |
   | 环境变量 | `MIMO_API_KEY` |

5. 点击 "部署"

### 第四步：测试 Plugin

1. 在 Plugin 配置页面，找到 "测试" 功能
2. 使用以下请求测试：

   ```json
   {
     "model": "mimo-v2.5-tts",
     "text": "你好，这是测试文本。",
     "voice": "白桦"
   }
   ```

3. 检查响应：
   - 状态码：200
   - 返回 `audio_url` 或 `audio_base64`

4. 如果测试失败，检查：
   - API Key 是否正确
   - 网络连接是否正常
   - 请求格式是否正确

### 第五步：创建 Bot

1. 在 Coze 控制台，点击 "创建 Bot"
2. 填写基本信息：

   | 字段 | 值 |
   |:-----|:---|
   | 名称 | AI 读书伴侣 (BookBuddy) |
   | 描述 | 让读书变成愉悦、享受、沉浸的体验 |
   | Logo | 上传你的 Logo |

3. 添加 Plugin：
   - 点击 "添加 Plugin"
   - 选择 "BookBuddy TTS"
   - 配置默认参数

4. 配置 Bot 指令：
   - 复制 `bot-config.json` 中的 `system_prompt`
   - 粘贴到 Bot 的 "指令" 字段

5. 配置开场白：
   - 复制 `bot-config.json` 中的 `user_greeting`
   - 粘贴到 Bot 的 "开场白" 字段

### 第六步：发布 Plugin

1. 在 Plugin 配置页面，点击 "提交审核"
2. 填写审核信息：
   - 功能描述
   - 使用场景
   - 用户群体

3. 等待审核（通常 1-3 天）

4. 审核通过后：
   - Plugin 发布到 Coze Store
   - 用户可以搜索并使用

## 🔧 环境变量配置

### 必需环境变量

| 变量名 | 描述 | 示例值 |
|:-------|:-----|:-------|
| `MIMO_API_KEY` | MiMo API Key | `sk-xxxxxxxxxxxxxxxxxxxx` |

### 可选环境变量

| 变量名 | 描述 | 默认值 |
|:-------|:-----|:-------|
| `PORT` | 服务端口 | `8080` |
| `LOG_LEVEL` | 日志级别 | `INFO` |
| `RATE_LIMIT` | 速率限制（请求/分钟） | `60` |

## 📊 监控和日志

### 查看日志

1. 在 Coze 控制台，进入 Plugin 页面
2. 点击 "日志" 标签
3. 查看实时日志

### 常用日志查询

```
# 查看所有请求
level=INFO

# 查看错误
level=ERROR

# 查看特定时间范围
time>=2024-01-01T00:00:00Z AND time<=2024-01-02T00:00:00Z
```

### 监控指标

| 指标 | 描述 | 告警阈值 |
|:-----|:-----|:---------|
| `requests_total` | 总请求数 | - |
| `requests_error_rate` | 错误率 | > 5% |
| `response_time_p99` | P99 响应时间 | > 10s |
| `api_key_invalid_rate` | 无效 API Key 率 | > 1% |

## 🛠️ 故障排除

### 常见问题

#### 1. API Key 无效

**错误信息**：
```
{"error": "无效的 API Key"}
```

**解决方案**：
1. 检查 `MIMO_API_KEY` 环境变量是否正确
2. 确认 API Key 格式：`sk-xxxxxxxxxxxxxxxxxxxx`
3. 在 MiMo 平台验证 API Key 是否有效

#### 2. 请求超时

**错误信息**：
```
{"error": "请求超时，请检查文本长度或重试"}
```

**解决方案**：
1. 减少文本长度
2. 增加超时时间（在云端函数配置中）
3. 使用批量生成模式分块处理

#### 3. 音色无效

**错误信息**：
```
{"error": "无效的 voice，可选值: 冰糖, 茉莉, 苏打, 白桦, Mia, Chloe, Milo, Dean"}
```

**解决方案**：
1. 检查音色名称是否正确
2. 使用 `GET /v1/voices` 获取可用音色列表
3. 注意大小写敏感

#### 4. 参考音频无效

**错误信息**：
```
{"error": "voice_reference_audio 参数不能为空（需要 5 秒以上的参考音频）"}
```

**解决方案**：
1. 确保上传了音频文件
2. 音频时长至少 5 秒
3. 音频格式：MP3、WAV、M4A
4. 音频质量：16kHz 以上采样率

#### 5. 云端函数部署失败

**错误信息**：
```
Deployment failed: ...
```

**解决方案**：
1. 检查 `requirements.txt` 依赖是否有效
2. 检查 `main.py` 语法是否正确
3. 查看部署日志获取详细信息
4. 尝试重新部署

### 调试技巧

1. **启用调试日志**：
   ```python
   app.run(debug=True)
   ```

2. **本地测试**：
   ```bash
   # 安装依赖
   pip install -r requirements.txt
   
   # 设置环境变量
   export MIMO_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
   
   # 运行服务
   python main.py
   
   # 测试接口
   curl -X POST "http://localhost:8080/v1/tts/generate" \
     -H "Authorization: Bearer $MIMO_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"model": "mimo-v2.5-tts", "text": "测试"}'
   ```

3. **检查网络**：
   ```bash
   # 测试 MiMo API 连接
   curl -I "https://api.xiaomimimo.com/v1/chat/completions"
   ```

## 📈 性能优化

### 1. 缓存

启用响应缓存，减少重复请求：

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/v1/tts/generate", methods=["POST"])
@cache.cached(timeout=3600, key_prefix="tts")
def generate_audio():
    ...
```

### 2. 批量处理

使用批量生成模式处理长文本：

```json
{
  "model": "mimo-v2.5-tts",
  "text": "长文本...",
  "chunk_size": 300
}
```

### 3. 并发请求

并行生成多个音频片段：

```python
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=5)
# 并行提交请求
```

### 4. 资源限制

配置合理的资源限制：

| 资源 | 推荐值 |
|:-----|:-------|
| 内存 | 256MB - 512MB |
| 超时 | 60s - 120s |
| 并发 | 5 - 10 |

## 🔐 安全建议

1. **保护 API Key**：
   - 不要在前端代码中暴露 API Key
   - 使用环境变量管理
   - 定期轮换 API Key

2. **速率限制**：
   ```python
   from flask_limiter import Limiter
   
   limiter = Limiter(app, key_func=lambda: request.remote_addr)
   
   @app.route("/v1/tts/generate", methods=["POST"])
   @limiter.limit("60 per minute")
   def generate_audio():
       ...
   ```

3. **输入验证**：
   - 验证文本长度
   - 验证音频格式
   - 清理特殊字符

4. **HTTPS**：
   - 始终使用 HTTPS
   - 验证 SSL 证书

## 📝 更新日志

### v1.0.0 (2024-01-01)

- 初始版本
- 支持三种 TTS 模式
- 支持 8 种内置音色
- 支持 6 种声音设计预设
- 支持声音克隆
- 批量生成支持

---

**需要帮助？**

- GitHub Issues: https://github.com/lssuzie/bookbuddy/issues
- 文档: https://github.com/lssuzie/bookbuddy/blob/main/README.md