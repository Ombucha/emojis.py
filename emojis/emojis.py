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


with open("database/data.json", encoding="utf-8") as file:
    data = json.loads(file.read())

data_from_emoji = {}
for item in data:
    data_from_emoji[item["emoji"]] = item

    if "skins" in item:
        for skin in item["skins"]:
            data_from_emoji[skin["emoji"]] = skin

with open("database/messages.json", encoding="utf-8") as file:
    messages = json.loads(file.read())

group_from_order = {}
for item in messages["groups"]:
    group_from_order[item["order"]] = item

subgroup_from_order = {}
for item in messages["subgroups"]:
    subgroup_from_order[item["order"]] = item

with open("database/shortcodes.json", encoding="utf-8") as file:
    shortcodes = json.loads(file.read())


class Emoji:

    """
    A class that represents an emoji.

    Parameters
    ----------
    :param emoji: The emoji's symbol (character).
    :type emoji: str

    Attributes
    ----------
    :ivar emoji: The emoji character.
    :ivar label: The label or description of the emoji.
    :ivar hexcode: The Unicode hexcode of the emoji.
    :ivar gender: The gender associated with the emoji, if any.
    :ivar version: The Unicode version in which the emoji was introduced.
    :ivar order: The ordering index of the emoji.
    :ivar group: The group/category of the emoji.
    :ivar subgroup: The subgroup/category of the emoji.
    :ivar tags: A list of tags associated with the emoji.
    :ivar type: The type of emoji (e.g., "standard", "modifier").
    :ivar skins: A list of Emoji objects representing skin tone variations.
    :ivar shortcodes: A list of shortcodes for the emoji.
    """

    def __init__(self, emoji: str) -> None:

        try:
            _data = data_from_emoji[emoji]
        except KeyError as exc:
            raise ValueError("Emoji not found in the database.") from exc

        self.emoji = emoji
        self.label = _data.get("label", None)
        self.hexcode = _data.get("hexcode", None)
        self.gender = _data.get("gender", None)
        self.version = _data.get("version", None)
        self.order = _data.get("order", None)
        self.group = _data.get("group", None)
        self.subgroup = _data.get("subgroup", None)
        self.tags = _data.get("tags", [])
        self.type = _data.get("type", None)
        self.skins = [Emoji(skin["emoji"]) for skin in _data.get("skins", [])]

        self.shortcodes = shortcodes.get(self.hexcode, [])
        if isinstance(self.shortcodes, str):
            self.shortcodes = [self.shortcodes]

    def __str__(self) -> str:
        return self.emoji

    def __repr__(self) -> str:
        return f"Emoji(emoji={self.emoji!r}, label={self.label!r}, hexcode={self.hexcode!r})"

    def __int__(self) -> int:
        return self.order

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Emoji):
            return NotImplemented
        return self.emoji == other.emoji

    def __hash__(self) -> int:
        return hash(self.emoji)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Emoji):
            return NotImplemented
        return self.order < other.order

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Emoji):
            return NotImplemented
        return self.order <= other.order

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Emoji):
            return NotImplemented
        return self.order > other.order

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Emoji):
            return NotImplemented
        return self.order >= other.order

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Emoji):
            return NotImplemented
        return self.emoji != other.emoji

class Group:

    """
    A class that represents a group of emojis.

    Parameters
    ----------
    :param order: The order index of the emoji group.
    :type order: int

    Attributes
    ----------
    :ivar order: The order index of the emoji group.
    :ivar name: The name of the emoji group.
    :ivar key: The key identifier for the group.
    :ivar emojis: A list of Emoji objects in this group.
    """

    def __init__(self, order: int) -> None:
        self.order = order
        self.name = group_from_order[order]["message"]
        self.key = group_from_order[order]["key"]
        self.emojis = {Emoji(key) for key, value in data_from_emoji.items() if value.get("group", None) == order}

    def __str__(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"Group(name={self.name!r}, order={self.order!r})"

    def __int__(self) -> int:
        return self.order

    def __len__(self) -> int:
        return len(self.emojis)

    def __contains__(self, item: Emoji) -> bool:
        if not isinstance(item, Emoji):
            return NotImplemented
        return item in self.emojis

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return NotImplemented
        return self.order == other.order

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return NotImplemented
        return self.order < other.order

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return NotImplemented
        return self.order <= other.order

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return NotImplemented
        return self.order > other.order

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return NotImplemented
        return self.order >= other.order

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return NotImplemented
        return self.order != other.order

class Subgroup:

    """
    A class that represents a subgroup of emojis within a group.

    Parameters
    ----------
    :param order: The order index of the emoji subgroup.
    :type order: int

    Attributes
    ----------
    :ivar order: The order index of the emoji subgroup.
    :ivar name: The name of the emoji subgroup.
    :ivar key: The key identifier for the subgroup.
    :ivar emojis: A list of Emoji objects in this subgroup.
    """

    def __init__(self, order: int) -> None:
        self.order = order
        self.name = subgroup_from_order[order]["message"]
        self.key = subgroup_from_order[order]["key"]
        self.emojis = {Emoji(key) for key, value in data_from_emoji.items() if value.get("subgroup", None) == order}

    def __str__(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"Subgroup(name={self.name!r}, order={self.order!r})"

    def __int__(self) -> int:
        return self.order

    def __len__(self) -> int:
        return len(self.emojis)

    def __contains__(self, item: Emoji) -> bool:
        if not isinstance(item, Emoji):
            return NotImplemented
        return item in self.emojis

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Subgroup):
            return NotImplemented
        return self.order == other.order

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Subgroup):
            return NotImplemented
        return self.order < other.order

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Subgroup):
            return NotImplemented
        return self.order <= other.order

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Subgroup):
            return NotImplemented
        return self.order > other.order

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Subgroup):
            return NotImplemented
        return self.order >= other.order

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Subgroup):
            return NotImplemented
        return self.order != other.order
