import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="m>")

modules = [
  "modules.fun",
  "modules.info",
  "modules.owner",
  "modules.nsfw"
]

for module in modules:
  bot.load_extension(module)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="m>help"))
  print("Name: %s" % (bot.user.name))
  print("ID: %s" % (bot.user.id))
  print("discord.py (rewrite) version: %s" % (discord.__version__))
  print("--------------------------------------")

bot.run(str(os.environ.get("TOKEN")))
