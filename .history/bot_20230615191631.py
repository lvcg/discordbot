import os
from dotenv import load_dotenv
import discord

# Configure the desired intents for the bot
intents = discord.Intents.default()
intents.typing = False  # Disable the typing indicator
intents.presences = False  # Disable receiving member presences (requires privileged gateway intents)

# Create the Discord client with the specified intents
client = discord.Client(intents=intents)

# Load environment variables from a .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
# Event handler for when the bot is ready and connected to Discord

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    
    print(
        f'{client.user} is connected to  the  following guild:\n'
        f'{guild.name}(id:)'
          

# Run the bot with the provided token
client.run(TOKEN)

