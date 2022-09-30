import discord
from discord.ext import commands
from requests import get
from json import loads

help_value = "Get A Random Motivating Quote :)"
help_syntax = "Usage: `r!quote`"
def get_quote():
    response = get("https://zenquotes.io/api/random")
    json_data = loads(response.text)
    quotes = json_data[0]['q'] + "-" + json_data[0]['a']
    return (quotes)

class Quote(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    @commands.command()
    async def quote(self,ctx):
          quote = get_quote()
          embed = discord.Embed()
          embed.title = "Rander Quotes"
          embed.description = quote
          embed.set_footer(text="Requested By {} ".format(ctx.message.author.name))
          await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Quote(client))