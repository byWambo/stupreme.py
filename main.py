# Invite: https://discordapp.com/api/oauth2/authorize?client_id=494559639036231685&permissions=8&scope=bot

import discord
from utils import config
from discord.ext import commands
import logging
import random

fmt = '[%(levelname)s] %(asctime)s - %(name)s:%(lineno)d - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)

bot_config = config.Config()
settings = bot_config.create()

bot = commands.Bot(command_prefix=settings["prefix"], owner_id=settings["owner_id"])

cogs = [
    'cogs.commands'
]

for cog in cogs:
    bot.load_extension(cog)
    
play_list = ["a game", "with Barbie <3", "with Stupreme Merch", "with Dome", "with Wambo"]


@bot.event
async def on_ready():
    logging.info('------------------Logged in as " + bot.user.name + " (" + bot.user.id + ")------------------')
    logging.info("\n".join([f"{s.name} ({str(s.id)})" for s in bot.guilds]))
    await bot.change_presence(activity=discord.Game(name=random.choice(play_list))

bot.run(settings["token"])
