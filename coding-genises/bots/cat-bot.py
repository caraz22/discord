import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

global total_messages
total_messages = 0
global cat_gifs
cat_gifs = 0

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    global total_messages
    total_messages += 1
    global cat_gifs

    ratio = 0

    if ((("cat" in message.content) or ("kitty" in message.content)) and ("tenor.com" in message.content)):
        cat_gifs += 1
    
    if message.content == "!count":
        await message.channel.send("ᨐᵉᵒʷ! The total number of messages is " + str(total_messages))
    if message.content == "!cats":
        await message.channel.send("ᨐᵉᵒʷ! The total number of cat gifs is " + str(cat_gifs))
    if message.content == "!compare":
        await message.channel.send("ᨐᵉᵒʷ! The ratio of cat gifs to all messages is " + str(ratio))

bot.run(BOT_TOKEN)