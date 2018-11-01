import discord
from discord.ext import commands

class Info:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    await ctx.send("🏓 Pong! **(%s ms)**" % (round(self.bot.latency * 1000)))

  @commands.command()
  async def botinfo(self, ctx):
    emb = discord.Embed(colour=discord.Colour.green())
    emb.set_author(name="My Info", icon_url=self.bot.user.avatar_url)
    emb.add_field(name="Name", value="%s" % (self.bot.user.name), inline=False)
    emb.add_field(name="ID", value="%s" % (self.bot.user.id), inline=False)
    emb.add_field(name="Lib", value="discord.py (rewrite) [%s]" % (discord.__version__), inline=False)
    emb.set_footer(text="Requested by %s" % (ctx.author.name))

    await ctx.send(embed=emb)

def setup(bot):
  bot.add_cog(Info(bot))
