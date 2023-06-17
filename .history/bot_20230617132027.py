# bot.py
import os

import discord
from discord.ext import commands
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.typing = False  # Disable the typing indicator
intents.presences = False  # Disable receiving member presences (requires privileged gateway intents)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # Use the discord.utils.find() function to search for a guild (server) in the client's guilds list
    # The lambda function is used as the search condition, comparing the name of each guild with the value of the variable GUILD
    # Assign the found guild to the variable 'guild'
    guild = discord.utils.get(client.guilds, name=GUILD)

    if guild is not None:
        # Print a message indicating which guild the bot is connected to, along with its name and ID
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    else:
        print(f'The bot is not connected to the guild: {GUILD}')

client.run(TOKEN)

