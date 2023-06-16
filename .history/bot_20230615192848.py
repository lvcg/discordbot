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
#The event is triggered when the bot has successfully connected to Discord and is ready to start interacting.
# Event handler for when the bot is ready and connected to Discord


@client.event
async def on_ready():
    # The on_ready event handler function

    guild = discord.utils.find(lambda g: g.name )
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # Print a message indicating which guild the bot is connected to, along with its name and ID
      
      
    # Create a list comprehension that iterates over each member in the guild's members list and retrieves their names
    # Join the names together with a newline and a hyphen using the join() method
    # Assign the resulting string to the variable 'members'
    # members = '\n - '.join([member.name for member in guild.members])


    # Print a formatted string that displays the label "Guild Members:", followed by the members' names with a hyphen before each name
    # The '\n' creates a newline to separate the label from the members' names
    # print(f'Guild Members:\n - {members}')



# Run the bot with the provided token
client.run(TOKEN)

