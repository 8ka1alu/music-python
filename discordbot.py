import discord
import os 

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

#----------これより下にbotの動作----------

#----------これより上にbotの動作----------

client.run(TOKEN)
