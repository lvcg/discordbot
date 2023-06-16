# bot.py 
import os 

import discord
intents = discord.Intents.default()
intents.typing = False  # Disable the typing indicator
intents.presences = False  # Disable receiving member presences (requires privileged gateway intents)

client = discord.Client(intents=intents)
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
client.run(TOKEN)