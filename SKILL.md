---
name: everything-to-podcast
description: "将任何文本内容（PDF、EPUB、TXT、Markdown、网页）转换为高质量有声书或播客音频。支持两种模式：AI代读模式（AI读完总结后生成播客）和直接转音频模式（全文逐字朗读）。当用户提到：有声书、播客、转音频、朗读、听书、TTS、text to speech、audio、audiobook、语音合成、耳朵阅读、眼睛疲劳、护眼阅读、或者给你一本书/论文/文档让你读，都应使用此技能。"
---

# 万物播客 Everything-to-Podcast

> 万物皆可转播客。AI 时代更个性化的阅读方式，更沉浸式的阅读体验。

本技能将文本内容转换为高质量有声书或播客音频。配合 AI Agent 使用时，支持两种互补的工作模式。

---

## 两种模式

### 模式一：AI 代读 + 播客生成

当用户给你一本书、小说集、论文、文档，说"帮我读一下"、"总结一下"、"生成播客"时：

1. **读完全文**：逐篇/逐章阅读用户给的文件
2. **口语化总结**：用讲故事的方式，把每篇内容讲给用户听——不是干巴巴的摘要，是像朋友聊天一样讲故事
3. **评估打分**（如果用户需要）：根据用户的需求（比如"哪篇最适合改编短片"）给出分析和排名
4. **生成播客**：把总结文本保存为 Markdown，然后调用 TTS 脚本生成音频
5. **告知结果**：告诉用户音频文件位置和时长

**播客文本的写作要求**：
- 像跟朋友聊天一样讲故事，不要写成分析报告
- 先讲故事本身（发生了什么），再给评价（好不好、值不值得读）
- 每篇控制在 300-500 字，口语化，有节奏感
- 适合朗读：短句为主，少用括号和破折号，读出来要顺口

### 模式二：直接转有声书（全文朗读）

当用户想把一篇文章、论文、完整书籍转成有声书时：

1. **读取文件**：支持 PDF、EPUB、TXT、Markdown
2. **清洗文本**：去 Markdown 格式、修正编码
3. **调用 TTS 脚本**：`python3 <skill-path>/scripts/generate_audio.py <输入文件> -o <输出文件>`
4. **告知结果**：音频文件位置和时长

---

## 快速使用

### 安装

```bash
npx skills add lssuzie/everything-to-podcast
```

### 命令行使用

```bash
# 基础用法：输入 md/txt，输出同名 mp3
python3 scripts/generate_audio.py my_book.md

# 指定输出路径和音色
python3 scripts/generate_audio.py my_book.md -o output.mp3 -v 白桦

# 快速模式（1.2倍速，适合内容扫描）
python3 scripts/generate_audio.py my_book.md --fast

# 指定 API Key
MIMO_API_KEY=tp-xxx python3 scripts/generate_audio.py my_book.md
```

### 需要的依赖

- **MiMo API Key**：从 `.env` 文件读取（支持 `~/.gemini/antigravity/scratch/.env` 或 `--env` 参数），也可通过环境变量 `MIMO_API_KEY` 传入
- **ffmpeg**：用于合并音频分段（`brew install ffmpeg`）

---

## 技术说明（给想深入了解的人）

### 为什么需要按句切片（100 字上限）？

TTS 模型在处理长文本时，注意力误差会累积，导致后半段出现飘音、电音、语速失控。将每次合成限制在 100 字以内，并在句号、问号、感叹号处断句，保证模型始终在最佳状态推理，语调自然不断裂。

### 为什么需要 NFKC 编码修正？

PDF/OCR 提取的中文文本中，部分汉字会被映射到"康熙部首"字符集（视觉相同但编码不同），导致 TTS 引擎读音错乱。`unicodedata.normalize("NFKC", text)` 自动修正。

### 断点续传

脚本自动检测已生成的分段文件，中断后重新运行会跳过已完成的部分。每 30 段自动合并为一个分卷 MP3，防止数据丢失。

详细技术文档参见 `references/` 目录。

---

> [!WARNING]
> 本技能及配套脚本仅限个人学习、研究与技术交流使用，**严禁用于任何商业用途**。
