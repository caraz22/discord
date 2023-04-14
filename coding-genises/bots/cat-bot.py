import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    global total_messages
    total_messages = 0

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    total_messages += 1

    if message.content.startswith('!count'):
        await message.channel.send(total_messages)

@bot.command()
async def count(ctx):
    if ctx.content.includes('count'):
        await ctx.channel.send(total_messages)

bot.run(BOT_TOKEN)