emojis.py
==========

Installation
------------

**Python 3.8 or higher is required.**

To install the stable version, do the following:

.. code-block:: sh

    # Unix / macOS
    python3 -m pip install "emojis.py"

    # Windows
    py -m pip install "emojis.py"


To install the development version, do the following:

.. code-block:: sh

    $ git clone https://github.com/Ombucha/emojis.py

Make sure you have the latest version of Python installed, or if you prefer, a Python version of 3.8 or greater.

If you have have any other issues feel free to search for duplicates and then create a new issue on GitHub with as much detail as possible. Include the output in your terminal, your OS details and Python version.


Emoji
-----

.. autoclass:: emojis.Emoji
    :members:


Group
-----

.. autoclass:: emojis.Group
    :members:


Subgroup
-----

.. autoclass:: emojis.Subgroup
    :members:


Utility Functions
----------------

.. autofunction:: emojis.is_emoji
.. autofunction:: emojis.emoji_count
.. autofunction:: emojis.get_emoji_from_name
.. autofunction:: emojis.get_emoji_from_hexcode
.. autofunction:: emojis.get_emoji_from_shortcode
.. autofunction:: emojis.get_emoji_from_order
.. autofunction:: emojis.get_all_emojis
.. autofunction:: emojis.emojize
.. autofunction:: emojis.demojize
.. autofunction:: emojis.get_group
.. autofunction:: emojis.get_subgroup
.. autofunction:: emojis.get_all_groups
.. autofunction:: emojis.get_all_subgroups
.. autofunction:: emojis.emoji_kitchen
.. autofunction:: emojis.search_emojis
