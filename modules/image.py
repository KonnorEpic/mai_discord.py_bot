import discord
from discord.ext import commands

class Image:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def achievement(self, ctx):
    txt = ctx.message.content[14:].replace(" ", "%20")
    genUrl = "https://minecraftskinstealer.com/achievement/a.php?i=2&h=Achievement+Get%21&t=%s" % (txt)
    try:
      emb = discord.Embed(title="Achievement Generator", colour=discord.Colour.green())
      emb.set_image(url=genUrl)
      emb.set_footer(text="Requested by %s" % (ctx.author.name))
      
      await ctx.send(embed=emb)
    except:
      await ctx.send("You not provided text.")

def setup(bot):
  bot.add_cog(Image(bot))
