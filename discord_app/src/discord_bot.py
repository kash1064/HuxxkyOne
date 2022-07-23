import discord

from config.environ_config import env
from discord_actions import *

# Discord App
DISCORD_TOKEN = env("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print("Bot is loggin")
    await client.connect("", reconnect=True)¶
    return

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "/bow":
        await message.channel.send("わんわん")
        return

    return

client.run(DISCORD_TOKEN)