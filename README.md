# 🎙️ 万物播客 Everything-to-Podcast

> **万物皆可转播客。AI 时代更个性化的阅读方式，更沉浸式的阅读体验。**
> 
> 书读不完？AI 帮你读，再讲给你听。

[![GitHub stars](https://img.shields.io/github/stars/lssuzie/text-to-audiobook.svg?style=flat-square)](https://github.com/lssuzie/text-to-audiobook/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/lssuzie/text-to-audiobook.svg?style=flat-square)](https://github.com/lssuzie/text-to-audiobook/network)

[中文](#-万物播客) | [English](#-everything-to-podcast)

---

## 🇨🇳 万物播客

### 你有没有过这种经历？

- 买了一本书，翻了两页就吃灰了
- 下载了一堆 epub，从来没打开过
- 论文/报告堆成山，根本看不完
- 买了书觉得愧疚，不买又忍不住

**不是不想读，是读不动。**

### 万物播客怎么帮你？

万物播客不是又一个 TTS 工具。它是一个 **「万物转播客」工作流**——配合 AI Agent（Claude Code 等），把任何内容变成可听的播客：

```
你有内容（书/论文/文档）
       ↓
AI 帮你读完、总结、分析
       ↓
生成播客音频（男声/女声，带感情）
       ↓
戴上耳机，通勤路上听完
```

### 一个真实案例

我有一本短篇小说集，19 篇故事，3500 行，读不下去。

我让 Claude Code 读了整本书，逐篇讲给我听——每篇故事讲了什么、核心冲突是什么、情感基调怎么样。然后 AI 帮我打了分：哪篇最适合改编短片。

最后我把 AI 写的故事梗概转成音频，**20 分钟的播客，通勤路上就听完了**。

一本书，我一个字没读，但全书脉络了然于胸。

**这才是万物播客的核心价值：不是替代阅读，是替代「读不下去」。**

### 两种玩法，任你选

碎片化时代，越来越没耐心读长文本了。万物播客提供两种互补的听读方式：

**玩法一：万物播客 — 快速扫描**
> 书读不完？让 AI 帮你读，再讲给你听。

把 epub/pdf/md 喂给 AI，AI 读完逐篇总结，再转成 20 分钟左右的播客音频。通勤路上听完，全书脉络了然于胸。定位是**快速扫描**——不用精读，先用播客做全书概览。

**玩法二：护眼有声书 — 深度精读**
> 每天盯着屏幕 Vibe Coding，眼睛真的要报废了。对真正重要的书，用你喜欢的声线逐字"读"给你听。

对重要的书、论文、原文，用你喜欢的声线（甚至自己的声线），喜欢的节奏和语调（磁性的、沙哑的、冥想感的），生成完整的有声书。睡前听、通勤听，用耳朵逐字"阅读"。这不是替代阅读，是**全新的阅读方式**。

**两种模式互补：先听播客快速扫描全书 → 挑出值得精读的篇目 → 生成有声书深度阅读。**

### 万物播客能做什么？

| 场景 | 怎么用 |
|------|--------|
| 小说集/散文集 | AI 逐篇总结，生成播客，先听再决定读哪篇 |
| 技术书籍 | AI 提取核心论点，生成音频边听边理解 |
| 论文/报告 | AI 总结方法和结论，快速判断相关性 |
| 会议纪要 | 长文档转语音，通勤时"听完"工作材料 |
| 新闻/文章合集 | 批量喂给 AI，生成每日新闻播客 |

### 快速开始

```bash
# 安装技能
npx skills add lssuzie/text-to-audiobook

# 告诉 AI 你的文件路径，然后说：
# "帮我读这本书，总结每篇故事，生成播客"
```

就这么简单。剩下的交给 AI。

### 技术细节（给想折腾的人）

如果你好奇背后的原理，或者想自己定制：

1. **280 字切片**：防止 TTS 在长文本上"读飘"——电音、加速、吞字
2. **NFKC 编码修正**：PDF/OCR 提取的乱码字自动纠正为标准汉字
3. **断点续传**：跑到一半断网了？重跑自动跳过已生成的段落
4. **多格式支持**：PDF、EPUB、TXT、Markdown 都能吃
5. **音色可选**：白桦（磁性男声）等多种音色，支持声音克隆

### 为什么叫「万物播客」？

因为不只是书。论文、报告、会议纪要、新闻合集、甚至你微信里收藏的那些长文——**任何文字内容都可以变成播客**。

AI 负责读和总结，TTS 负责读出来，你负责戴着耳机听。

这就是「万物播客」：让耳朵成为你的眼睛。

---

## 🇺🇸 Everything-to-Podcast

> **Turn anything into a podcast. A more personal, immersive way to read in the AI era.**
> 
> Can't finish a book? Let AI read it, then tell you about it.

### The Problem

- Books collecting dust on your shelf
- EPUBs downloaded but never opened
- Papers and reports piling up
- You feel guilty for not reading, but you just can't get through them

**It's not that you don't want to read. You just can't.**

### How Everything-to-Podcast Helps

This isn't another TTS tool. It's a **workflow**: combine AI Agents (Claude Code, etc.) with high-quality speech synthesis to turn any content into a listenable podcast.

```
You have content (book / paper / document)
       ↓
AI reads, summarizes, and analyzes it
       ↓
Generates podcast audio (male/female voice, with emotion)
       ↓
Put on your ears, listen on your commute
```

### Two Ways to Use It

We live in an age of information overload and shrinking attention spans. Everything-to-Podcast offers two complementary ways to listen and learn:

**Way 1: AI-Powered Podcast — Fast Scan**
> Can't finish a book? Let AI read it, then tell you about it.

Feed your epub/pdf/md to AI. It reads the whole thing, summarizes each chapter, and generates a ~20-minute podcast. Listen on your commute — you'll know the entire book without reading a page. This is **fast scanning** — skip deep reading, get the full picture first.

**Way 2: Eye-Saver Audiobooks — Deep Reading**
> Staring at screens all day for Vibe Coding? Your eyes are dying. For the books that truly matter, listen to every word in a voice you love.

For important books, papers, and original texts — generate a full audiobook in a voice you love (even your own), at a pace and tone that suits you (magnetic, gravelly, meditative). Listen before bed, on your commute. Let your ears "read" word by word. This isn't replacing reading — it's **an entirely new way to read**.

**The two modes work together: listen to the podcast for a fast scan → pick the chapters worth deep reading → generate an audiobook for deep immersion.**

### A Real Example

I had a short story collection — 19 stories, 3,500 lines. Couldn't finish it.

I had Claude Code read the entire book, summarize each story — plot, core conflict, emotional tone. AI scored and ranked them ("which is best for film adaptation?").

Then I converted the summaries to audio. **A 20-minute podcast, done during one commute.**

I didn't read a single page, but I knew the entire book.

**That's the core value: not replacing reading, but replacing "never getting around to reading."**

### Quick Start

```bash
npx skills add lssuzie/text-to-audiobook
```

Then tell your AI Agent: "Read this book, summarize each chapter, and generate a podcast."

### Technical Details

For those who want to dig deeper:

1. **280-char slicing** — prevents TTS audio degradation on long texts
2. **NFKC normalization** — fixes CJK pronunciation glitches from OCR/PDF sources
3. **Checkpoint resume** — picks up where it left off after interruptions
4. **Multi-format** — PDF, EPUB, TXT, Markdown all supported
5. **Voice options** — multiple voices including voice cloning support

---

## 🧑‍💻 Contributing

PRs and Issues welcome! / 欢迎提交 PR 和 Issue。

### Stats

<p align="left">
  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img height="180" src="https://github-readme-stats.vercel.app/api?username=lssuzie&show_icons=true&theme=radial" alt="lssuzie's GitHub stats" />
  </a>
  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=lssuzie&layout=compact&theme=radial" alt="Top Langs" />
  </a>
</p>

---

> [!WARNING]
> **免责声明 / Disclaimer**
> 本技能及配套脚本仅限个人学习、研究与技术交流使用，**严禁用于任何商业用途**。因违规商用或传播有版权音频所导致的任何侵权纠纷，均由使用者本人承担。
> 
> This skill is for personal learning and research only. **Any commercial use is strictly prohibited.**

*License: CC BY-NC-SA 4.0*
