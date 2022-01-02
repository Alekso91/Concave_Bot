import uuid
import discord
from settings import *

client = discord.Client()

@client.event
async def on_ready():
    print("\nBot is operational as {0.user}".format(client))

@client.event
async def on_message(message):
    if words_to_scan in message.content and message.author!=client.user:
        channel = client.get_channel(NowPlayingChannelID)
        await channel.send(message.content)

client.run(discordBotToken)