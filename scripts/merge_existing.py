import os
import subprocess

def merge_existing_audio():
    scratch_dir = "/Users/lushu/.gemini/antigravity/scratch"
    temp_dir = os.path.join(scratch_dir, "temp_audio_parts")
    output_mp3 = "/Users/lushu/Documents/爱呀河有声书/爱呀河谜案录 有声书_已生成部分.mp3"
    
    if not os.path.exists(temp_dir):
        print(f"❌ 错误: 找不到临时缓存目录 {temp_dir}。这说明目前没有任何已生成的分段。")
        return
        
    # 获取所有临时分段并排序
    parts = [f for f in os.listdir(temp_dir) if f.startswith("part_") and f.endswith(".mp3")]
    parts.sort()
    
    if not parts:
        print("❌ 错误: 临时缓存目录中目前没有任何音频分段。")
        return
        
    print(f"🎬 发现已生成的分段数量: {len(parts)} (从 {parts[0]} 到 {parts[-1]})")
    print("正在生成临时合并清单...")
    
    filelist_path = os.path.join(temp_dir, "filelist_existing.txt")
    with open(filelist_path, "w", encoding="utf-8") as f:
        for p in parts:
            full_path = os.path.join(temp_dir, p)
            f.write(f"file '{full_path}'\n")
            
    print("正在使用 ffmpeg 无损合并已生成的部分...")
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", filelist_path, "-c", "copy", output_mp3
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"\n🎉 成功! 已将前 {len(parts)} 段合并导出为:")
            print(f"📁 {output_mp3}")
            print("\n💡 提示: 原本的临时分段文件未被删除，您可以在网络恢复后随时继续运行 generate_audio.py 进行断点续传合成全本。")
        else:
            print(f"❌ 合并失败 (ffmpeg 报错): {result.stderr}")
    except Exception as e:
        print(f"❌ 异常: {e}")
    finally:
        if os.path.exists(filelist_path):
            os.remove(filelist_path)

if __name__ == "__main__":
    merge_existing_audio()
