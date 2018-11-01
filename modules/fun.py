import random
import discord
from discord.ext import commands

from data import lists

class Fun:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def coinflip(self, ctx):
    coins = random.choice(lists.coins)

    await ctx.send("**%s** flipped a coin and got **%s**!" % (ctx.author.name, coins))

  @commands.command()
  async def say(self, ctx):
    txt = ctx.message.content[6:]
    try:
      await ctx.send(txt)
    except:
      await ctx.send("You not provided text.")

  @commands.command()
  async def spacetext(self, ctx):
    txt = ctx.message.content[12:].replace("", " ")
    try:
      await ctx.send(txt)
    except:
      await ctx.send("You not provided text.")

def setup(bot):
  bot.add_cog(Fun(bot))
