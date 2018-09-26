# Invite: https://discordapp.com/api/oauth2/authorize?client_id=494559639036231685&permissions=8&scope=bot

import discord
from utils import config
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)

bot_config = config.Config()
settings = bot_config.create()

bot = commands.Bot(command_prefix=settings["prefix"], owner_id=settings["owner_id"])

cogs = [
    'cogs.commands'
]

for cog in cogs:
    bot.load_extension(cog)


@bot.event
async def on_ready():
    logging.info('------------------Logged in as " + bot.user.name + " (" + bot.user.id + ")------------------')
    logging.info("\n".join([f"{s.name} ({str(s.id)})" for s in bot.guilds]))
    await bot.change_presence(activity=discord.Game(name="a game"))

bot.run(settings["token"])
