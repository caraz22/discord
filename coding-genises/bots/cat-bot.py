import discord
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
global CHANNEL_ID
CHANNEL_ID = os.environ.get("CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

global total_messages
total_messages = 0
global cat_gifs
cat_gifs = 0
global percentage

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

    if ((("cat" in message.content) or ("kitty" in message.content)) and ("tenor.com" in message.content)):
        cat_gifs += 1

    global percentage
    
    if message.content == "!count":
        total_messages -= 1        
        await message.channel.send("ᨐᵉᵒʷ! The total number of messages is " + str(total_messages))
    if message.content == "!cats":
        total_messages -= 1        
        await message.channel.send("ᨐᵉᵒʷ! The total number of cat gifs is " + str(cat_gifs))
    if message.content == "!compare":
        total_messages -= 1
        if total_messages == 0:
            percentage = 0
        else:
            percentage = (cat_gifs / total_messages) * 100
        await message.channel.send("ᨐᵉᵒʷ! The percentage of cat gifs to all messages is " + str(percentage) + "%")

bot.run(BOT_TOKEN)