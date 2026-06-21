# Skill 声音指南

## 核心：找到你的声音，然后调速度

BookBuddy 不是切换音色的工具。**你找到一个喜欢的声音，然后通过调速度和演绎方式来适应不同场景。**

```bash
# 找到声音
python3 generate_audio.py 书.md --voice-design "温柔私语"

# 调速度适应场景
python3 generate_audio.py 论文.md --voice-design "温柔私语"           # 1.0x
python3 generate_audio.py 故事.md --voice-design "温柔私语" -s 0.9    # 0.9x
python3 generate_audio.py 播客.md --voice-design "温柔私语" -s 1.1    # 1.1x
python3 generate_audio.py 睡前.md --voice-design "温柔私语" -s 0.7    # 0.7x
```

---

## 声音设计预设（试听用）

| 预设 | 声线 | 
|:-----|:-----|
| **温柔私语** 👑 | 温暖磁性，自然亲切 |
| **知识讲述** | 沉稳清晰，像老师在娓娓道来 |
| **故事演绎** | 有戏剧张力，能演绎情绪 |
| **播客主持** | 自然亲切，像朋友在聊天 |
| **睡前陪伴** | 温柔缓慢，越来越轻 |
| **冥想引导** | 空灵安宁，像从远处传来 |

---

## 内置音色

| 音色 | 语言 | 性别 | 感觉 |
|:-----|:----:|:----:|:-----|
| 冰糖 | 中文 | 女 | 清亮甜美 |
| 茉莉 | 中文 | 女 | 温柔知性 |
| 苏打 | 中文 | 男 | 清爽活力 |
| 白桦 | 中文 | 男 | 沉稳磁性 |
| Mia | 英文 | 女 | Bright |
| Chloe | 英文 | 女 | Warm |
| Milo | 英文 | 男 | Deep |
| Dean | 英文 | 男 | Calm |

---

## 自定义声音描述

```bash
# 描述你喜欢的风格
python3 generate_audio.py book.txt --voice-design "温暖甜美有气质的女声，像知性偶像在娓娓道来"

# 自定义演绎方式（声音不变）
python3 generate_audio.py book.txt --voice-design "温暖甜美有气质的女声" \
  --design-prompt "用沉稳专业的语气朗读"
```

**描述维度：**
- 性别：男/女/中性
- 年龄：少年/青年/中年/老年
- 质感：磁性/沙哑/清亮/醇厚/柔和
- 风格：温暖/沉稳/元气/神秘/严肃

---

## 声音克隆

```bash
python3 generate_audio.py book.txt --voice-clone --ref-audio 参考音频.mp3
```

**参考音频要求：** 5-8 秒，清晰朗读，无背景音乐，16kHz 以上。

**克隆提示词：**
```bash
--clone-prompt "标准流利普通话"
--clone-prompt "温暖亲切"
```

**克隆后也可以调速度：**
```bash
python3 generate_audio.py 睡前.md --voice-clone --ref-audio 我的声音.mp3 -s 0.7
```