import discord
from discord.ext import commands
from emojis import is_emoji, emoji_count, get_emoji_from_name, search_emojis

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    try:
        await tree.sync()
    except Exception as e:
        print(e)

@tree.command(name="isemoji")
async def isemoji(interaction: discord.Interaction, char: str):
    await interaction.response.send_message(f"{char} is an emoji: {is_emoji(char)}")

@tree.command(name="count")
async def count(interaction: discord.Interaction, text: str):
    count = emoji_count(text)
    await interaction.response.send_message(f"Emoji count: {count}")

@tree.command(name="lookup")
async def lookup(interaction: discord.Interaction, name: str):
    try:
        emoji = get_emoji_from_name(name)
        await interaction.response.send_message(f"Emoji for '{name}': {emoji.emoji}")
    except Exception as e:
        await interaction.response.send_message(str(e))

@tree.command(name="search")
async def search(interaction: discord.Interaction, query: str):
    results = search_emojis(query)
    if results:
        await interaction.response.send_message(" ".join(e.emoji for e in results[:20]))
    else:
        await interaction.response.send_message("No emojis found.")

bot.run("token")
