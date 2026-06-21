#!/usr/bin/env python3
"""generate_audio.py 纯函数单元测试"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from generate_audio import clean_text, split_text, build_tts_payload, build_voice_design_payload


class TestCleanText(unittest.TestCase):
    def test_nfkc_normalization(self):
        self.assertEqual(clean_text("ＡＢＣ"), "ABC")

    def test_removes_separators(self):
        # 分隔线被移除，留下空行
        self.assertEqual(clean_text("前文\n----\n后文"), "前文\n\n后文")
        self.assertEqual(clean_text("前文\n****\n后文"), "前文\n\n后文")
        self.assertEqual(clean_text("前文\n====\n后文"), "前文\n\n后文")

    def test_removes_full_end_tag(self):
        self.assertEqual(clean_text("正文[全文完]"), "正文")

    def test_removes_urls(self):
        # URL 被移除，多余空格被合并
        self.assertEqual(clean_text("访问 https://example.com/path 获取"), "访问 获取")

    def test_removes_arrows(self):
        self.assertEqual(clean_text("方向→左边←回来"), "方向左边回来")

    def test_merges_hard_wraps(self):
        self.assertEqual(clean_text("第一行\n第二行"), "第一行第二行")

    def test_preserves_sentence_boundary(self):
        result = clean_text("第一句。\n第二句")
        self.assertIn("第一句。", result)
        self.assertIn("第二句", result)

    def test_collapses_multiple_blank_lines(self):
        result = clean_text("段落一\n\n\n\n段落二")
        self.assertNotIn("\n\n\n", result)

    def test_collapses_multiple_spaces(self):
        self.assertEqual(clean_text("a  b   c"), "a b c")

    def test_strips_whitespace(self):
        self.assertEqual(clean_text("  hello  "), "hello")

    def test_empty_input(self):
        self.assertEqual(clean_text(""), "")


class TestSplitText(unittest.TestCase):
    def test_basic_split(self):
        chunks = split_text("句一。句二。句三。", max_len=10)
        self.assertTrue(all(len(c) <= 10 for c in chunks))
        self.assertEqual("".join(chunks), "句一。句二。句三。")

    def test_long_sentence_stays_intact(self):
        long_sent = "这" * 50 + "。"
        chunks = split_text(long_sent, max_len=10)
        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0], long_sent)

    def test_empty_input(self):
        self.assertEqual(split_text("", max_len=10), [])

    def test_only_whitespace(self):
        self.assertEqual(split_text("   \n  ", max_len=10), [])

    def test_custom_max_len(self):
        text = "一二三。四五六。七八九。"
        chunks = split_text(text, max_len=6)
        self.assertTrue(all(len(c) <= 6 for c in chunks))

    def test_no_split_when_under_limit(self):
        chunks = split_text("短句。", max_len=100)
        self.assertEqual(len(chunks), 1)

    def test_exclamation_and_question_marks(self):
        chunks = split_text("问？答！好。", max_len=5)
        self.assertGreaterEqual(len(chunks), 2)


class TestBuildTtsPayload(unittest.TestCase):
    def test_basic_structure(self):
        p = build_tts_payload("你好", "白桦")
        self.assertEqual(p["model"], "mimo-v2.5-tts")
        self.assertEqual(p["audio"]["voice"], "白桦")
        self.assertEqual(p["audio"]["speed"], 1.0)
        self.assertEqual(p["audio"]["format"], "mp3")

    def test_custom_speed(self):
        p = build_tts_payload("你好", "冰糖", speed=1.2)
        self.assertEqual(p["audio"]["speed"], 1.2)
        self.assertIn("1.2倍", p["messages"][0]["content"])

    def test_default_speed_no_speed_instruction(self):
        p = build_tts_payload("你好", "白桦", speed=1.0)
        self.assertNotIn("1.2倍", p["messages"][0]["content"])

    def test_text_optimized_with_comma(self):
        p = build_tts_payload("句一。句二。", "白桦")
        self.assertIn("。， ", p["messages"][1]["content"])

    def test_assistant_role_for_text(self):
        p = build_tts_payload("朗读这段", "白桦")
        self.assertEqual(p["messages"][1]["role"], "assistant")
        self.assertEqual(p["messages"][1]["content"], "朗读这段")

    def test_prompt_mentions_voice_id(self):
        p = build_tts_payload("text", "Mia")
        self.assertIn("Mia", p["messages"][0]["content"])


class TestBuildVoiceDesignPayload(unittest.TestCase):
    def test_basic_structure(self):
        p = build_voice_design_payload("你好", "温暖女声", "")
        self.assertEqual(p["model"], "mimo-v2.5-tts-voicedesign")
        self.assertEqual(p["messages"][0]["content"], "温暖女声")
        self.assertEqual(p["messages"][1]["content"], "你好")
        self.assertTrue(p["audio"]["optimize_text_preview"])

    def test_with_style_prompt(self):
        p = build_voice_design_payload("你好", "温暖女声", "用平静语气朗读")
        content = p["messages"][0]["content"]
        self.assertIn("温暖女声", content)
        self.assertIn("用平静语气朗读", content)

    def test_without_style_prompt(self):
        p = build_voice_design_payload("你好", "温暖女声", None)
        self.assertEqual(p["messages"][0]["content"], "温暖女声")

    def test_custom_speed(self):
        p = build_voice_design_payload("你好", "desc", "", speed=0.8)
        self.assertEqual(p["audio"]["speed"], 0.8)


if __name__ == "__main__":
    unittest.main()
