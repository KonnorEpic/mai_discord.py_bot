import discord
from discord.ext import commands

class Owner:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def logout(self, ctx):
    if ctx.author.id == 416540213696004117:
      await ctx.send("👋 Bye.")
      await self.bot.logout()
    else:
      await ctx.send("You not my owner.")

def setup(bot):
  bot.add_cog(Owner(bot))