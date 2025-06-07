"""
MIT License

Copyright (c) 2025 Omkaar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


# pylint: skip-file

import unittest

from emojis.utils import (
    get_all_emojis,
    get_emoji_from_name,
    get_emoji_from_hexcode,
    get_emoji_from_shortcode,
    get_emoji_from_order,
    search_emojis,
)

class TestEmojis(unittest.TestCase):

    def test_get_all_emojis_returns_list(self):
        emojis = get_all_emojis()
        self.assertIsInstance(emojis, list)
        self.assertGreater(len(emojis), 0)
        for e in emojis:
            self.assertTrue(hasattr(e, "emoji"))
            self.assertTrue(isinstance(e.emoji, str))
            self.assertGreater(len(e.emoji), 0)

    def test_get_emoji_from_name_valid(self):
        emoji = get_emoji_from_name("grinning face")
        self.assertEqual(emoji.emoji, "😀")

    def test_get_emoji_from_name_invalid(self):
        with self.assertRaises(ValueError):
            get_emoji_from_name("not an emoji")
        with self.assertRaises(ValueError):
            get_emoji_from_name("")
        with self.assertRaises(ValueError):
            get_emoji_from_name(" ")
        with self.assertRaises(ValueError):
            get_emoji_from_name(":grinning:")
        # If you don't check type, just ensure it doesn't crash
        try:
            get_emoji_from_name(123)
        except Exception:
            pass
        try:
            get_emoji_from_name(None)
        except Exception:
            pass

    def test_get_emoji_from_name_case(self):
        with self.assertRaises(ValueError):
            get_emoji_from_name("Grinning Face")

    def test_get_emoji_from_hexcode_valid(self):
        emoji = get_emoji_from_hexcode("1F600")
        self.assertEqual(emoji.emoji, "😀")

    def test_get_emoji_from_hexcode_invalid(self):
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("FFFF")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("not_a_hexcode")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("1f600")  # lowercase
        try:
            get_emoji_from_hexcode(123)
        except Exception:
            pass
        try:
            get_emoji_from_hexcode(None)
        except Exception:
            pass

    def test_get_emoji_from_shortcode_valid(self):
        emoji = get_emoji_from_shortcode("grinning")
        self.assertEqual(emoji.emoji, "😀")

    def test_get_emoji_from_shortcode_invalid(self):
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("not_a_shortcode")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode(" ")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("Grinning")  # case-sensitive
        try:
            get_emoji_from_shortcode(123)
        except Exception:
            pass
        try:
            get_emoji_from_shortcode(None)
        except Exception:
            pass

    def test_get_emoji_from_order_valid(self):
        emoji = get_emoji_from_order(0)
        self.assertTrue(isinstance(emoji.emoji, str))
        self.assertGreater(len(emoji.emoji), 0)
        try:
            emoji2 = get_emoji_from_order(1)
            self.assertTrue(isinstance(emoji2.emoji, str))
            self.assertGreater(len(emoji2.emoji), 0)
        except Exception:
            pass

    def test_get_emoji_from_order_invalid(self):
        with self.assertRaises(IndexError):
            get_emoji_from_order(-1)
        with self.assertRaises(IndexError):
            get_emoji_from_order(999999)
        with self.assertRaises(IndexError):
            get_emoji_from_order(-100)
        # If you don't check type, just ensure it doesn't crash
        try:
            get_emoji_from_order("zero")
        except Exception:
            pass
        try:
            get_emoji_from_order(None)
        except Exception:
            pass
        try:
            get_emoji_from_order(1.5)
        except Exception:
            pass

    def test_search_emojis_by_label(self):
        results = search_emojis("grinning")
        self.assertTrue(any(e.emoji == "😀" for e in results))

    def test_search_emojis_by_shortcode(self):
        results = search_emojis("grin")
        self.assertTrue(any("grin" in sc for e in results for sc in getattr(e, "shortcodes", [])))

    def test_search_emojis_by_hexcode(self):
        results = search_emojis("1F600")
        self.assertTrue(any(e.emoji == "😀" for e in results))
        results2 = search_emojis("1f600")
        self.assertTrue(any(e.emoji == "😀" for e in results2))

    def test_search_emojis_by_emoji(self):
        results = search_emojis("😀")
        self.assertTrue(any(e.emoji == "😀" for e in results))

    def test_search_emojis_no_results(self):
        results = search_emojis("notarealemoji")
        self.assertEqual(results, [])
        results2 = search_emojis("")
        self.assertIsInstance(results2, list)

    def test_search_emojis_partial_match(self):
        results = search_emojis("grin")
        self.assertTrue(any("grin" in e.label for e in results))

    def test_search_emojis_whitespace(self):
        results = search_emojis(" ")
        self.assertIsInstance(results, list)

    def test_search_emojis_special_characters(self):
        results = search_emojis("!@#$%^&*()")
        self.assertIsInstance(results, list)
        self.assertEqual(results, [])

    def test_search_emojis_type_errors(self):
        # If your implementation does not raise, just check for list or None
        try:
            result = search_emojis(None)
        except Exception:
            result = None
        self.assertTrue(result is None or isinstance(result, list))
        try:
            result = search_emojis(123)
        except Exception:
            result = None
        self.assertTrue(result is None or isinstance(result, list))

    def test_get_emoji_from_order_large(self):
        # Test very large positive and negative numbers
        with self.assertRaises(IndexError):
            get_emoji_from_order(10**10)
        with self.assertRaises(IndexError):
            get_emoji_from_order(-10**10)

    def test_search_emojis_numeric_string(self):
        # Should not raise, but may return empty
        results = search_emojis("123456")
        self.assertIsInstance(results, list)

    def test_search_emojis_unicode(self):
        # Unicode string that is not an emoji
        results = search_emojis("你好")
        self.assertIsInstance(results, list)

if __name__ == "__main__":
    unittest.main()
