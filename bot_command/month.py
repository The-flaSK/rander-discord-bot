import discord
from calendar import month
from discord.ext import commands

help_value = "Get All Dates And Days Of Required Month From A Year"
help_syntx = "Usage: `r!month` `<year>` `<month>`"
class Month(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    @commands.command()
    async def month(self,ctx, year: int, monthe: int):
         calen = month(year, monthe, 3, 1)
         embed = discord.Embed(title="Calendar", description=f"{calen}")
         await ctx.send(embed=embed) 
         
def setup(client):
    client.add_cog(Month(client))