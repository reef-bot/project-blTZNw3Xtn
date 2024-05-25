# main.py

# This is the main Python file for the moderation bot

import discord
from bot import Bot

# Create a new Discord client
client = discord.Client()

# Create an instance of the Bot class
bot = Bot(client)

# Event for when the bot is ready
@client.event
async def on_ready():
    print('Bot is ready.')

# Event for when a message is received
@client.event
async def on_message(message):
    await bot.process_message(message)

# Run the bot with the specified Discord bot token
client.run('YOUR_DISCORD_BOT_TOKEN')