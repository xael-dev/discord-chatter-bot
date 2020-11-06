import os
from discord.ext import commands
from settings import *
import logging

bot = commands.Bot(command_prefix="~")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

logging.basicConfig(level=logging.DEBUG)

bot.run(DISCORD_BOT_TOKEN)
