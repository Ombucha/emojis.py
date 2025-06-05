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


import json

from .emojis import Emoji, Group, Subgroup


with open("database/data.json", encoding="utf-8") as file:
    data = json.loads(file.read())

data_from_emoji = {}
for item in data:
    data_from_emoji[item["emoji"]] = item

    if "skins" in item:
        for skin in item["skins"]:
            data_from_emoji[skin["emoji"]] = skin

with open("database/metadata.json", encoding="utf-8") as file:
    metadata = json.loads(file.read())

with open("database/shortcodes.json", encoding="utf-8") as file:
    shortcodes = json.loads(file.read())

shortcodes_from_shortcode = {}
for item in shortcodes:
    if isinstance(shortcodes[item], str):
        shortcodes[item] = [shortcodes[item]]
    for shortcode in shortcodes[item]:
        shortcodes_from_shortcode[shortcode] = item


def is_emoji(character: str) -> bool:
    """
    Check if a character is an emoji.

    :param character: The character to check.
    :type character: str
    :return: True if the character is an emoji, False otherwise.
    :rtype: bool
    """
    return character in data_from_emoji

def emoji_count(text: str) -> int:
    """
    Count the number of emojis in a given text.

    :param text: The text to count emojis in.
    :type text: str
    :return: The number of emojis in the text.
    :rtype: int
    """
    return sum(1 for char in text if is_emoji(char))

def get_emoji_from_name(name: str) -> Emoji:
    """
    Get the emoji character from its name.

    :param name: The name of the emoji.
    :type name: str
    :return: An Emoji object if found.
    :rtype: Emoji
    """
    for item in data:
        if item["label"] == name:
            return Emoji(item["emoji"])
    raise ValueError(f"Emoji with name '{name}' not found.")

def get_emoji_from_hexcode(hexcode: str) -> Emoji:
    """
    Get the emoji character from its hexcode.

    :param hexcode: The hexcode of the emoji.
    :type hexcode: str
    :return: An Emoji object if found.
    :rtype: Emoji
    """
    for item in data:
        if item["hexcode"] == hexcode:
            return Emoji(item["emoji"])
    raise ValueError(f"Emoji with hexcode '{hexcode}' not found.")

def get_emoji_from_shortcode(shortcode: str) -> Emoji:
    """
    Get the emoji character from its shortcode.

    :param shortcode: The shortcode of the emoji.
    :type shortcode: str
    :return: An Emoji object if found.
    :rtype: Emoji
    """
    hexcode = shortcodes_from_shortcode.get(shortcode)
    if hexcode:
        return get_emoji_from_hexcode(hexcode)
    raise ValueError(f"Emoji with shortcode '{shortcode}' not found.")

def get_emoji_from_order(order: int) -> Emoji:
    """
    Get the emoji character from its order in the database.

    :param order: The order index of the emoji.
    :type order: int
    :return: An Emoji object if found.
    :rtype: Emoji
    """
    if 0 <= order < len(data):
        return Emoji(data[order]["emoji"])
    raise IndexError(f"Order '{order}' is out of range.")

def get_all_emojis() -> list:
    """
    Get a list of all emoji characters.

    :return: A list of all emoji characters.
    :rtype: list
    """
    return [Emoji(item["emoji"]) for item in data]

def emojize(text: str) -> str:
    """
    Convert shortcodes in the text to emojis.

    :param text: The text containing shortcodes.
    :type text: str
    :return: The text with shortcodes replaced by emojis.
    :rtype: str
    """
    for key, value in shortcodes_from_shortcode.items():
        text = text.replace(f":{key}:",  "".join(chr(int(emoji, 16)) for emoji in value.split("-")))
    return text

def demojize(text: str) -> str:
    """
    Convert emojis in the text to shortcodes.

    .. note::

            This function only replaces emojis with the alphabetically first shortcode if multiple shortcodes exist for the same emoji.

    :param text: The text containing emojis.
    :type text: str
    :return: The text with emojis replaced by shortcodes.
    :rtype: str
    """
    for key, value in shortcodes.items():
        text = text.replace("".join(chr(int(emoji, 16)) for emoji in key.split("-")), f":{value[0]}:")
    return text

def get_group(emoji: Emoji) -> Group:
    """
    Get the group of an emoji.

    :param emoji: The Emoji object.
    :type emoji: Emoji
    :return: The Group object containing the emoji.
    :rtype: Group
    """
    return Group(emoji.group)

def get_subgroup(emoji: Emoji) -> Subgroup:
    """
    Get the subgroup of an emoji.

    :param emoji: The Emoji object.
    :type emoji: Emoji
    :return: The Subgroup object containing the emoji.
    :rtype: Subgroup
    """
    return Subgroup(emoji.subgroup)

def get_all_groups() -> list:
    """
    Get a list of all emoji groups.

    :return: A list of Group objects.
    :rtype: list
    """
    return [Group(order) for order in range(10)]

def get_all_subgroups() -> list:
    """
    Get a list of all emoji subgroups.

    :return: A list of Subgroup objects.
    :rtype: list
    """
    return [Subgroup(order) for order in range(100)]

def emoji_kitchen(emoji1: Emoji, emoji2: Emoji) -> str:
    """
    Combine two emojis to create a new emoji.

    .. note::

            This function utilises Google's Emoji Kitchen feature to combine two emojis.

    :param emoji1: The first Emoji object.
    :type emoji1: Emoji
    :param emoji2: The second Emoji object.
    :type emoji2: Emoji
    :return: The link to the combined emoji.
    :rtype: str
    """
    return metadata["data"][emoji1.hexcode.lower()]["combinations"][emoji2.hexcode.lower()][0]["gStaticUrl"]

def search_emojis(query: str) -> list:
    """
    Search for emojis by name or shortcode.

    :param query: The search query (name or shortcode).
    :type query: str
    :return: A list of Emoji objects that match the query.
    :rtype: list
    """
    results = []
    for item in get_all_emojis():
        if query.lower() in item.label.lower() or query.lower() in item.shortcodes or query.lower() in item.hexcode.lower() or query.lower() in item.emoji or query.lower() in item.tags:
            results.append(item)
    return results
