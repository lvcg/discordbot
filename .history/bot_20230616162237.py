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

# The event is triggered when the bot has successfully connected to Discord and is ready to start interacting.
# Event handler for when the bot is ready and connected to Discord
@client.event
async def on_ready():
    # The on_ready event handler function
    
   
    # Assign the found guild to the variable 'guild'
    guild = discord.utils.get(client.guilds, name=GUILD)

    # Print a message indicating which guild the bot is connected to, along with its name and ID
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    

# Run the bot with the provided token
client.run(TOKEN)


