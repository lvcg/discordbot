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
async def hello(ctx):
    await ctx.send('Hello, I am your friendly Discord bot!')
    
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
    print(f'Connected to Discord!')

@bot.event
async def on_guild_join(guild):
    print(f'Joined server: {guild.name}')

@bot.event
async def on_guild_remove(guild):
    print(f'Removed from server: {guild.name}')

bot.run(TOKEN)

