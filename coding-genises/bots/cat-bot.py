import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.bot(intents=intents)
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(BOT_TOKEN)