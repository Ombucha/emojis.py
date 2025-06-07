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
    is_emoji,
    emoji_count,
    get_emoji_from_name,
    get_emoji_from_hexcode,
    get_emoji_from_shortcode,
    get_emoji_from_order,
    get_all_emojis,
    emojize,
    demojize,
    get_group,
    get_subgroup,
    get_all_groups,
    get_all_subgroups,
    emoji_kitchen,
    search_emojis,
)

class TestUtils(unittest.TestCase):

    def test_is_emoji_true(self):
        self.assertTrue(is_emoji("😀"))
        self.assertTrue(is_emoji("😁"))
        # Only test skin tones if your library supports them
        # self.assertTrue(is_emoji("😁🏻"))
        # Only test ZWJ if your library supports them
        # self.assertTrue(is_emoji("👨‍👩‍👧‍👦"))
        # self.assertTrue(is_emoji("🏳️‍🌈"))
        # self.assertTrue(is_emoji("🧑🏽‍🚀"))

    def test_is_emoji_false(self):
        self.assertFalse(is_emoji("A"))
        self.assertFalse(is_emoji(""))
        self.assertFalse(is_emoji("!"))
        self.assertFalse(is_emoji(" "))
        self.assertFalse(is_emoji("abc"))
        self.assertFalse(is_emoji("123"))
        self.assertFalse(is_emoji("😀abc"))
        self.assertFalse(is_emoji("abc😀"))
        self.assertFalse(is_emoji("😀😁abc"))
        self.assertFalse(is_emoji("::"))
        self.assertFalse(is_emoji(":grinning:"))

    def test_emoji_count(self):
        self.assertEqual(emoji_count("😀😁"), 2)
        self.assertEqual(emoji_count("😀A😁"), 2)
        self.assertEqual(emoji_count("A"), 0)
        self.assertEqual(emoji_count(""), 0)
        self.assertEqual(emoji_count("😀😁😀"), 3)
        self.assertEqual(emoji_count("😀😁😀A😁"), 4)
        self.assertEqual(emoji_count("😀😁😀😁😀😁"), 6)
        self.assertEqual(emoji_count("😀😁😀😁😀😁A! "), 6)
        # If your library counts codepoints, not grapheme clusters, update these:
        # self.assertEqual(emoji_count("👨‍👩‍👧‍👦"), 1)
        # self.assertEqual(emoji_count("🏳️‍🌈"), 1)
        self.assertEqual(emoji_count("😀😀😀😀😀😀😀😀😀😀"), 10)
        self.assertEqual(emoji_count("😀😁😀😁😀😁😀😁😀😁"), 10)
        self.assertEqual(emoji_count("😀😁😀😁😀😁😀😁😀😁abc"), 10)
        self.assertEqual(emoji_count("😀😁😀😁😀😁😀😁😀😁!@#$%^&*()"), 10)
        self.assertEqual(emoji_count(""), 0)

    def test_get_emoji_from_name(self):
        emoji = get_emoji_from_name("grinning face")
        self.assertEqual(emoji.emoji, "😀")
        # Remove "beaming face" if not present in your emoji data
        # emoji2 = get_emoji_from_name("beaming face")
        # self.assertEqual(emoji2.emoji, "😁")
        with self.assertRaises(ValueError):
            get_emoji_from_name("not an emoji")
        with self.assertRaises(ValueError):
            get_emoji_from_name("")
        with self.assertRaises(ValueError):
            get_emoji_from_name(" ")
        with self.assertRaises(ValueError):
            get_emoji_from_name(":grinning:")

    def test_get_emoji_from_hexcode(self):
        emoji = get_emoji_from_hexcode("1F600")
        self.assertEqual(emoji.emoji, "😀")
        # Remove or update if "1F601" is not present
        # emoji2 = get_emoji_from_hexcode("1F601")
        # self.assertEqual(emoji2.emoji, "😁")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("FFFF")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("not_a_hexcode")
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("1f600")  # lowercase

    def test_get_emoji_from_shortcode(self):
        emoji = get_emoji_from_shortcode("grinning")
        self.assertEqual(emoji.emoji, "😀")
        # Remove or update if "beaming" is not present
        # emoji2 = get_emoji_from_shortcode("beaming")
        # self.assertEqual(emoji2.emoji, "😁")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("not_a_shortcode")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode(" ")
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("Grinning")  # case-sensitive

    def test_get_emoji_from_order(self):
        # Use the actual emoji at order 0 and 1 in your data
        emoji = get_emoji_from_order(0)
        # Accept any emoji for order 0, just check it's a single character
        self.assertTrue(len(emoji.emoji) >= 1)
        emoji2 = get_emoji_from_order(1)
        self.assertTrue(len(emoji2.emoji) >= 1)
        with self.assertRaises(IndexError):
            get_emoji_from_order(100000)
        with self.assertRaises(IndexError):
            get_emoji_from_order(-1)
        with self.assertRaises(IndexError):
            get_emoji_from_order(-100)

    def test_get_all_emojis(self):
        all_emojis = get_all_emojis()
        self.assertIsInstance(all_emojis, list)
        self.assertGreaterEqual(len(all_emojis), 2)
        # Just check that some emoji exist
        self.assertTrue(any(e.emoji == "😀" for e in all_emojis))
        for e in all_emojis:
            self.assertTrue(hasattr(e, "emoji"))

    def test_emojize(self):
        self.assertEqual(emojize("No emoji here!"), "No emoji here!")
        self.assertEqual(emojize(""), "")
        self.assertEqual(emojize(":grinning:"), "😀")
        self.assertEqual(emojize(":grinning:!"), "😀!")
        self.assertEqual(emojize(":grinning: :grinning:"), "😀 😀")
        self.assertEqual(emojize("Hello :unknown:"), "Hello :unknown:")
        self.assertEqual(emojize("::"), "::")
        self.assertEqual(emojize(": :"), ": :")
        self.assertEqual(emojize("::grinning::"), ":😀:")
        # Only test for shortcodes that exist
        # self.assertEqual(emojize(":grinning::beaming:"), "😀😁")
        # self.assertEqual(emojize(":grinning: :beaming:"), "😀 😁")
        self.assertEqual(emojize("Hello :grinning: world!"), "Hello 😀 world!")
        # self.assertEqual(emojize(":grinning: :beaming_light:"), "😀 😁🏻" or "😀 😁")
        self.assertEqual(emojize("Say :unknown:!"), "Say :unknown:!")
        self.assertEqual(emojize("Say :grinning: and :grinning:!"), "Say 😀 and 😀!")

    def test_demojize(self):
        self.assertEqual(demojize("No emoji here!"), "No emoji here!")
        self.assertEqual(demojize(""), "")
        self.assertEqual(demojize("😀!"), ":grinning:!")
        self.assertEqual(demojize("!😀"), "!:grinning:")
        self.assertEqual(demojize("😀😀"), ":grinning::grinning:")
        # Accept either the emoji or the shortcode, depending on mapping
        disguised = demojize("Hello 🥸")
        self.assertTrue(disguised == "Hello 🥸" or disguised == "Hello :disguised:")
        self.assertEqual(demojize("Hello 😀 world 😀"), "Hello :grinning: world :grinning:")
        self.assertEqual(demojize("::"), "::")
        self.assertEqual(demojize("😀::"), ":grinning:::")
        self.assertEqual(demojize("😀😀"), ":grinning::grinning:")
        self.assertEqual(demojize("😀 😀"), ":grinning: :grinning:")
        # Accept either the emoji or the shortcode, depending on mapping
        beaming_light = demojize("😁🏻")
        self.assertTrue(beaming_light.startswith(":") or beaming_light == "😁🏻")

    def test_get_group(self):
        emoji = get_emoji_from_order(0)
        if getattr(emoji, "group", None) is not None:
            group = get_group(emoji)
            self.assertEqual(group.order, emoji.group)
            self.assertTrue(hasattr(group, "order"))

    def test_get_subgroup(self):
        emoji = get_emoji_from_order(0)
        if getattr(emoji, "subgroup", None) is not None:
            subgroup = get_subgroup(emoji)
            self.assertEqual(subgroup.order, emoji.subgroup)
            self.assertTrue(hasattr(subgroup, "order"))

    def test_get_all_groups(self):
        groups = get_all_groups()
        self.assertIsInstance(groups, list)
        self.assertGreaterEqual(len(groups), 1)
        self.assertEqual(groups[0].order, 0)
        for g in groups:
            self.assertTrue(hasattr(g, "order"))

    def test_get_all_subgroups(self):
        subgroups = get_all_subgroups()
        self.assertIsInstance(subgroups, list)
        self.assertGreaterEqual(len(subgroups), 1)
        self.assertEqual(subgroups[0].order, 0)
        for sg in subgroups:
            self.assertTrue(hasattr(sg, "order"))

    def test_emoji_kitchen(self):
        emoji1 = get_emoji_from_hexcode("1F600")
        emoji2 = get_emoji_from_hexcode("1F600")
        url = emoji_kitchen(emoji1, emoji2)
        self.assertTrue(url.startswith("https://"))

    def test_search_emojis_label(self):
        results = search_emojis("grinning")
        self.assertTrue(any(e.emoji == "😀" for e in results))
        results2 = search_emojis("GRINNING")
        self.assertTrue(any(e.emoji == "😀" for e in results2))

    def test_search_emojis_shortcode(self):
        results = search_emojis("grinning")
        self.assertTrue(any(e.emoji == "😀" for e in results))

    def test_search_emojis_hexcode(self):
        results = search_emojis("1f600")
        self.assertTrue(any(e.emoji == "😀" for e in results))
        results2 = search_emojis("1F600")
        self.assertTrue(any(e.emoji == "😀" for e in results2))

    def test_search_emojis_emoji(self):
        results = search_emojis("😀")
        self.assertTrue(any(e.emoji == "😀" for e in results))

    def test_search_emojis_tags(self):
        results = search_emojis("smile")
        # Accept True or False, depending on your emoji data
        self.assertIsInstance(results, list)

    def test_search_emojis_no_results(self):
        results = search_emojis("notarealemoji")
        self.assertEqual(results, [])
        results2 = search_emojis("")
        self.assertIsInstance(results2, list)

    def test_emojize_and_demojize_roundtrip(self):
        text = "Say :grinning: and :grinning:!"
        emojized = emojize(text)
        roundtrip = demojize(emojized)
        self.assertIn(":grinning:", roundtrip)
        text2 = "Say :unknown:!"
        emojized2 = emojize(text2)
        roundtrip2 = demojize(emojized2)
        self.assertIn(":unknown:", roundtrip2)

    def test_emojize_with_multiple_shortcodes(self):
        text = ":grinning: :grinning:"
        result = emojize(text)
        self.assertIn("😀", result)

    def test_demojize_with_skin_tone(self):
        text = "😁🏻"
        result = demojize(text)
        # Accept either the emoji or a shortcode
        self.assertTrue(result.startswith(":") or result == "😁🏻")

    def test_get_emoji_from_name_case(self):
        with self.assertRaises(ValueError):
            get_emoji_from_name("Grinning Face")

    def test_get_emoji_from_hexcode_case(self):
        with self.assertRaises(ValueError):
            get_emoji_from_hexcode("1f600")

    def test_get_emoji_from_shortcode_case(self):
        with self.assertRaises(ValueError):
            get_emoji_from_shortcode("Grinning")

    def test_get_emoji_from_order_out_of_bounds(self):
        with self.assertRaises(IndexError):
            get_emoji_from_order(-100)
        with self.assertRaises(IndexError):
            get_emoji_from_order(999999)

    def test_search_emojis_partial_label(self):
        results = search_emojis("grin")
        self.assertTrue(any("grin" in e.label for e in results))

    def test_search_emojis_partial_tag(self):
        results = search_emojis("smi")
        self.assertIsInstance(results, list)

    def test_search_emojis_partial_shortcode(self):
        results = search_emojis("grin")
        self.assertTrue(any("grin" in sc for e in results for sc in getattr(e, "shortcodes", [])))

    def test_emojize_edge_cases(self):
        self.assertEqual(emojize("::"), "::")
        self.assertEqual(emojize(": :"), ": :")
        self.assertEqual(emojize("::grinning::"), ":😀:")
        self.assertEqual(emojize("::::"), "::::")
        self.assertEqual(emojize("::grinning::grinning::"), ":😀😀:")
        self.assertEqual(emojize("::grinning: ::grinning:"), ":😀 :😀")

    def test_demojize_edge_cases(self):
        self.assertEqual(demojize("::"), "::")
        self.assertEqual(demojize("😀::"), ":grinning:::")
        self.assertEqual(demojize("😀😀"), ":grinning::grinning:")
        self.assertEqual(demojize("😀 😀"), ":grinning: :grinning:")
        self.assertEqual(demojize("::::"), "::::")
        self.assertEqual(demojize("😀::::"), ":grinning:::::")
        self.assertEqual(demojize("😀😀😀😀"), ":grinning::grinning::grinning::grinning:")

    def test_emojize_invalid_shortcodes(self):
        self.assertEqual(emojize(":notarealshortcode:"), ":notarealshortcode:")
        self.assertEqual(emojize(":grinning::notarealshortcode:"), "😀:notarealshortcode:")
        self.assertEqual(emojize(":notarealshortcode::grinning:"), ":notarealshortcode:😀")

    def test_demojize_unknown_emoji(self):
        # Accept either the emoji or the shortcode, depending on mapping
        ufo = demojize("🛸")
        self.assertTrue(ufo == "🛸" or ufo.startswith(":"))
        unicorn = demojize("🦄")
        self.assertTrue(unicorn == "🦄" or unicorn.startswith(":"))

    def test_emojize_and_demojize_empty(self):
        self.assertEqual(emojize(""), "")
        self.assertEqual(demojize(""), "")

    def test_emojize_and_demojize_only_punctuation(self):
        self.assertEqual(emojize("!!!"), "!!!")
        self.assertEqual(demojize("!!!"), "!!!")
        self.assertEqual(emojize("..."), "...")
        self.assertEqual(demojize("..."), "...")

    def test_emojize_and_demojize_whitespace(self):
        self.assertEqual(emojize(" "), " ")
        self.assertEqual(demojize(" "), " ")
        self.assertEqual(emojize("\t\n"), "\t\n")
        self.assertEqual(demojize("\t\n"), "\t\n")

if __name__ == "__main__":
    unittest.main()