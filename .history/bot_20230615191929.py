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
    # The on_ready event handler function

    for guild in client.guilds:
        # Iterate over the guilds the bot is a member of

        if guild.name == GUILD:
            # Check if the guild's name matches the specified GUILD name (assumed to be a constant or defined elsewhere)
            # This allows the code to identify a specific guild if needed

            break
            # Exit the loop since the desired guild has been found

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # Print a message indicating which guild the bot is connected to, along with its name and ID
          

# Run the bot with the provided token
client.run(TOKEN)

