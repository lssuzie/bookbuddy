import json
import os
import re
import shutil
import sys

def clean_title(title):
    # 去除各种网页小说水印
    title = re.sub(r'👻.*', '', title)
    title = re.sub(r'💄.*', '', title)
    title = re.sub(r'🍎.*', '', title)
    # 替换特殊字符以防止文件名非法
    title = re.sub(r'[\/:*?"<>|]', '_', title)
    return title.strip()

def get_chapter_mapping(project_dir):
    json_path = os.path.join(project_dir, "禅者的初心_正文切片.json")
    # 兼容其他书籍的切片命名，优先使用特定书名，没有则找目录下的第一个 .json
    if not os.path.exists(json_path):
        json_files = [f for f in os.listdir(project_dir) if f.endswith("_正文切片.json")]
        if json_files:
            json_path = os.path.join(project_dir, json_files[0])
        else:
            raise FileNotFoundError("未能在项目目录中找到切片 JSON 文件。")
            
    with open(json_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
        
    chunk_to_chapter = {}
    current_chapter = "序言"
    
    for c in chunks:
        text = c["text"].strip()
        is_title = False
        if text.startswith("序 ") or text.startswith("前言 ") or text.startswith("第") and ("部" in text or "章" in text):
            is_title = True
        elif re.match(r'^\d+\s+[一-龥]{2,}', text):
            is_title = True
            
        if is_title:
            current_chapter = clean_title(text)
            
        chunk_to_chapter[c["id"]] = current_chapter
        
    return chunk_to_chapter, len(chunks)

def rename_volumes(project_dir):
    try:
        chunk_to_chapter, total_chunks = get_chapter_mapping(project_dir)
    except Exception as e:
        print(f"❌ 错误: {e}")
        return
        
    volume_size = 30
    volume_names = []
    chapter_counts = {}
    
    # 1. 预分析各卷覆盖章节，并生成基础章节标签
    for idx in range(0, total_chunks, volume_size):
        vol_num = idx // volume_size + 1
        start_chunk = idx + 1
        end_chunk = min(idx + volume_size, total_chunks)
        
        chapters_in_vol = []
        for cid in range(start_chunk, end_chunk + 1):
            ch = chunk_to_chapter.get(cid, "未知章节")
            if ch not in chapters_in_vol:
                chapters_in_vol.append(ch)
                
        if len(chapters_in_vol) == 1:
            raw_label = chapters_in_vol[0]
        else:
            # 滤除通用的第一部、第二部等大纲标题，使具体章节更显眼
            filtered = [x for x in chapters_in_vol if not (x.startswith("第一部") or x.startswith("第二部") or x.startswith("第三部"))]
            if not filtered:
                filtered = chapters_in_vol
            
            if len(filtered) == 1:
                raw_label = filtered[0]
            elif len(filtered) == 2:
                raw_label = f"{filtered[0]} & {filtered[1]}"
            else:
                raw_label = f"{filtered[0]} 至 {filtered[-1]}"
                
        raw_label = re.sub(r'\s+', ' ', raw_label)
        volume_names.append((vol_num, start_chunk, end_chunk, raw_label))
        chapter_counts[raw_label] = chapter_counts.get(raw_label, 0) + 1
        
    # 2. 执行物理重命名，并自动解决重名冲突（加自增序号）
    resolved_chapter_indices = {}
    
    print(f"\n--- 正在分析并重命名 {project_dir} 下的分卷 mp3 ---")
    for vol_num, start_chunk, end_chunk, label in volume_names:
        total_occur = chapter_counts[label]
        
        if total_occur > 1:
            resolved_chapter_indices[label] = resolved_chapter_indices.get(label, 0) + 1
            final_label = f"{label}({resolved_chapter_indices[label]})"
        else:
            final_label = label
            
        # 兼容两种常见的分卷命名格式
        old_pattern_1 = f"禅者的初心_有声书_第{str(start_chunk).zfill(4)}到{str(end_chunk).zfill(4)}段.mp3"
        old_pattern_2 = f"有声书_第{str(start_chunk).zfill(4)}到{str(end_chunk).zfill(4)}段.mp3"
        
        old_path = os.path.join(project_dir, old_pattern_1)
        if not os.path.exists(old_path):
            old_path = os.path.join(project_dir, old_pattern_2)
            
        new_name = f"分卷{str(vol_num).zfill(2)}_{final_label}.mp3"
        new_path = os.path.join(project_dir, new_name)
        
        if os.path.exists(old_path):
            shutil.move(old_path, new_path)
            print(f"✅ 重命名成功: {os.path.basename(old_path)} -> {new_name}")
        else:
            print(f"⚠️ 未找到对应分段音频文件，跳过: 第{start_chunk}到{end_chunk}段")

if __name__ == "__main__":
    p_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    rename_volumes(p_dir)
