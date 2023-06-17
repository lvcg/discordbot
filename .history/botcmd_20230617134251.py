import discord
from discord.ext import commands
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.typing = False  # Disable typing events
intents.presences = False  # Disable presence events

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def chat(ctx, *, message):
    # Initialize the Hugging Face chatbot
    chatbot = pipeline('conversational')

    # Get the response from the chatbot
    response = chatbot(message)

    # Send the response back to Discord
    await ctx.send(response[0]['generated_text'])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Check if the bot is running and connected to Discord
@bot.event
async def on_connect():
    print(f'Connected to Discord!')

# Check if the bot has joined a server
@bot.event
async def on_guild_join(guild):
    print(f'Joined server: {guild.name}')

# Check if the bot has been removed from a server
@bot.event
async def on_guild_remove(guild):
    print(f'Removed from server: {guild.name}')

# Run the bot
bot.run(os.getenv('BOT_TOKEN'))

