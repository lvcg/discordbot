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
    
@bot.command()
async def sentiment(ctx, *, text):
    # Initialize the sentiment analysis pipeline
    classifier = pipeline('sentiment-analysis')

    # Perform sentiment analysis on the provided text
    result = classifier(text)

    # Extract the sentiment label and score from the result
    label = result[0]['label']
    score = result[0]['score']

    # Send the sentiment analysis result back to Discord
    await ctx.send(f'Sentiment Analysis Result: Label={label}, Score={score}')

@bot.command()
async def ner(ctx, *, text):
    # Initialize the named entity recognition pipeline
    ner_model = pipeline('ner')

    # Perform named entity recognition on the provided text
    entities = ner_model(text)

    # Create a response with the recognized entities and their tokens
    response = '\n'.join([f'Token: {entity["word"]}, Entity: {entity["entity"]}' for entity in entities])

    # Send the named entity recognition result back to Discord
    await ctx.send(f'Named Entity Recognition Result:\n{response}')


@bot.event
async def on_ready():
    # This event is triggered when the bot has successfully connected to Discord
    print(f'Logged in as {bot.user.name}')
    print(f'Connected to Discord!')

@bot.event
async def on_guild_join(guild):
    # This event is triggered when the bot joins a new server (guild)
    print(f'Joined server: {guild.name}')

@bot.event
async def on_guild_remove(guild):
    # This event is triggered when the bot is removed from a server (guild)
    print(f'Removed from server: {guild.name}')


# Run the bot
bot.run(TOKEN)


