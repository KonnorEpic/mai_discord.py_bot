import requests
import discord
from discord.ext import commands

class NSFW:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hentai(self, ctx):
    if ctx.channel.is_nsfw():
      res = requests.get("https://nekobot.xyz/api/image?type=hentai")
      data = res.json()
      
      emb = discord.Embed(title="Hentai successfully generate!")
      emb.set_image(url=data["message"])
      emb.set_footer(text="Requested by %s" % (ctx.author.name))
      
      await ctx.send(embed=emb)
    else:
      await ctx.send("This channel is not nsfw!")

def setup(bot):
  bot.add_cog(NSFW(bot))
