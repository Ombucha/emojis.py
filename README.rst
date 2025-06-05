.. image:: https://raw.githubusercontent.com/Ombucha/emojis.py/main/banner.png

.. image:: https://img.shields.io/pypi/v/emojis.py
    :target: https://pypi.python.org/pypi/emojis.py
    :alt: PyPI version
.. image:: https://img.shields.io/pypi/dm/emojis.py
    :target: https://pypi.python.org/pypi/emojis.py
    :alt: PyPI downloads
.. image:: https://sloc.xyz/github/Ombucha/emojis.py
    :target: https://github.com/Ombucha/emojis.py/graphs/contributors
    :alt: Lines of code
.. image:: https://img.shields.io/github/repo-size/Ombucha/emojis.py
    :target: https://github.com/Ombucha/emojis.py
    :alt: Repository size

| ✨ A lightweight, expressive emoji utility library for Python 💻🐍  
| 🎉 Supports emoji lookup, search, and emoji-kitchen-style combos — all offline and blazing fast ⚡  
| No dependencies — just pure emoji magic 🪄

🚀 Features
-----------

- 🔍 Emoji lookup by name, alias, unicode, hexcode, shortcode, or order
- 🧠 Fast emoji search by keyword, label, shortcode, or tag
- 🍳 Emoji Kitchen-style mashups (Google Emoji Kitchen)
- 🏷️ Convert between emoji and shortcode (emojize/demojize)
- 🧩 Emoji grouping and subgrouping
- 📦 Bundled emoji data, no internet required
- 🪄 Zero dependencies, pure Python

📖 Usage & Quick Start
----------------------

.. code-block:: python

    from emojis import (
        is_emoji, emoji_count,
        get_emoji_from_name, get_emoji_from_hexcode, get_emoji_from_shortcode, get_emoji_from_order,
        get_all_emojis, emojize, demojize,
        get_group, get_subgroup, get_all_groups, get_all_subgroups,
        emoji_kitchen, search_emojis, Emoji
    )

    # Check if a character is an emoji
    print(is_emoji("🔥"))  # True

    # Count emojis in a string
    print(emoji_count("I love 🍕 and 🐍!"))  # 2

    # Lookup emoji by name, hexcode, shortcode, or order
    print(get_emoji_from_name("grinning face").emoji)  # 😀
    print(get_emoji_from_hexcode("1F525").emoji)       # 🔥
    print(get_emoji_from_shortcode("fire").emoji)      # 🔥
    print(get_emoji_from_order(0).emoji)               # First emoji in database

    # List all emojis (print only emoji characters)
    all_emojis = get_all_emojis()
    print([e.emoji for e in all_emojis[:5]])  # ['😀', '😃', '😄', ...]

    # Convert shortcodes to emojis and vice versa
    print(emojize("I am :fire:!"))  # I am 🔥!
    print(demojize("I am 🔥!"))     # I am :fire:!

    # Emoji details and grouping
    emoji = Emoji("🦄")
    print(emoji.label)              # 'unicorn'
    print(get_group(emoji).name)    # Group name
    print(get_subgroup(emoji).name) # Subgroup name

    # List all groups and subgroups (print names)
    print([g.name for g in get_all_groups()])
    print([sg.name for sg in get_all_subgroups()])

    # Emoji Kitchen-style combo (returns a URL)
    print(emoji_kitchen(Emoji("🥲"), Emoji("😎")))

    # Search for emojis by keyword, label, shortcode, or tag (print emoji characters)
    print([e.emoji for e in search_emojis("cat")])     # ['🐱', '😺', ...]

📦 Included Emoji Data
----------------------

This library bundles static emoji data from:

- `emojibase.dev <https://emojibase.dev>`_ 🧠  
- `emoji-kitchen-backend by xsalazar <https://github.com/xsalazar/emoji-kitchen-backend>`_ 🍳

All data is included upfront — no runtime fetching or internet required 🔒

⚙️ Installation
---------------

**Requires Python 3.8+ 🐍**

To install the latest stable release:

.. code-block:: sh

    # Unix / macOS 🍎🐧
    python3 -m pip install "emojis.py"

    # Windows 🪟
    py -m pip install "emojis.py"

To install the development version:

.. code-block:: sh

    git clone https://github.com/Ombucha/emojis.py
    cd emojis.py
    pip install -e .

🙌 Contributing
---------------

Contributions are welcome!  
If you have suggestions, bug reports, or want to add features, please open an issue or submit a pull request on GitHub.

- Read the `Contributing Guide <https://github.com/Ombucha/emojis.py/blob/main/CONTRIBUTING.md>`_ for best practices.
- Make sure your code is tested and documented.
- Be kind and respectful in all interactions.

Thank you for helping make emojis.py better! 🎉

🔗 Links
--------

| 🔎 `Documentation <https://emoji.readthedocs.io>`_  
| 📦 `PyPI Package <https://pypi.org/project/emojis.py/>`_  
| 📝 `Unicode Full Emoji List <https://unicode.org/emoji/charts/full-emoji-list.html>`_  
| 🌐 `Emojipedia <https://emojipedia.org/>`_  
|

🧪 Explore, search, and play with emojis in Python — your code just got way more expressive! 😄🎨🚀