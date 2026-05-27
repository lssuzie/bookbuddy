import fitz
import re
import os

def clean_block_lines(lines):
    cleaned_lines = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        if i > 0 and cleaned_lines:
            # 检查前一行的末尾和当前行的开头是否都是英文/数字，是则补空格，否则直接拼接
            last_char = cleaned_lines[-1][-1] if cleaned_lines[-1] else ''
            first_char = line[0] if line else ''
            if re.match(r'[a-zA-Z0-9]', last_char) and re.match(r'[a-zA-Z0-9]', first_char):
                cleaned_lines.append(' ' + line)
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    return "".join(cleaned_lines)

def pdf_to_markdown(pdf_path, md_path):
    doc = fitz.open(pdf_path)
    markdown_content = []
    
    # 全书合法的排版字体集合
    valid_fonts = {'PingFangSC-Regular', 'TimesNewRomanPSMT'}
    
    print(f"Reading PDF: {pdf_path}, total {len(doc)} pages.")
    
    # 跳过第一页和第二页（封面和目录）
    for page_idx in range(2, len(doc)):
        page = doc[page_idx]
        text_dict = page.get_text("dict")
        
        # 提取有文本行的 blocks，并按照垂直坐标 y0, x0 排序
        text_blocks = [b for b in text_dict["blocks"] if "lines" in b]
        text_blocks.sort(key=lambda b: (round(b["bbox"][1], 1), round(b["bbox"][0], 1)))
        
        for b in text_blocks:
            block_lines = []
            for line in b["lines"]:
                line_text_parts = []
                for span in line["spans"]:
                    font = span["font"]
                    text = span["text"]
                    
                    # 精准过滤：只保留正文排版字体，抛弃所有手写识别出的系统私有/UI字体
                    if font in valid_fonts:
                        cleaned = text.strip()
                        if "CAA专阅" in cleaned:
                            continue
                        if cleaned == "-":
                            line_text_parts.append("\n---\n")
                            continue
                        line_text_parts.append(text)
                
                line_text = "".join(line_text_parts).strip()
                if line_text:
                    block_lines.append(line_text)
            
            # 清洗行首尾，将 block 中的行拼装成自然段
            if block_lines:
                cleaned_block = clean_block_lines(block_lines)
                if cleaned_block:
                    # 识别章节标题
                    if re.match(r'^【.+】$', cleaned_block):
                        markdown_content.append(f"\n\n# {cleaned_block}\n")
                    else:
                        markdown_content.append(f"\n{cleaned_block}\n")
                        
    # 拼接并进行最终格式修剪
    import unicodedata
    full_md = "".join(markdown_content)
    full_md = unicodedata.normalize("NFKC", full_md)
    # 合并连续的 3 个换行符为 2 个，保持段落间距一致
    full_md = re.sub(r'\n{3,}', '\n\n', full_md)
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_md.strip() + "\n")
        
    print(f"Successfully generated clean Markdown: {md_path}")

if __name__ == "__main__":
    pdf_path = "/Users/lushu/Documents/爱呀河有声书/爱呀河谜案录 短篇集（全文）.pdf"
    md_path = "/Users/lushu/Documents/爱呀河有声书/爱呀河谜案录 短篇集（全文）.md"
    pdf_to_markdown(pdf_path, md_path)
