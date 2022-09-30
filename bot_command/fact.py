import discord
from discord.ext import commands
import randfacts

help_value = "Get A Random Fact To Increase Your Knowledge"
help_syntax = "Usage:`r!fact`"
class Fact(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    @commands.command()
    async def fact(self,ctx):
       facts = randfacts.get_fact(True)
       embed = discord.Embed()
       embed.title = "Rander Facts"
       embed.description = facts
       embed.set_footer(text="Requested By {} ".format(ctx.message.author.name))
       await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fact(client))