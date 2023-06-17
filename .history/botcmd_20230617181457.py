# Import necessary libraries and modules
import discord
from discord.ext import commands
from transformers import pipeline
from dotenv import load_dotenv
import os
from transformers import AlbertTokenizer, AlbertModel

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Disable typing and presence events
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Initialize tokenizer and model
tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
model = AlbertModel.from_pretrained("albert-base-v2")

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Sample input for Albert model
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

# Define commands and events
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

# Run the bot
bot.run(TOKEN)


