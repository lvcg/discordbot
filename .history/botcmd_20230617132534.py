import discord
from discord.ext import commands
from transformers import pipeline

bot = commands.Bot(command_prefix='!')

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

# Run the bot
bot.run('YOUR_BOT_TOKEN')
