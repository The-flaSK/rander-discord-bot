import discord
from discord.ext import commands
from discord.embeds import Embed

help_value = "Get Latency Of Our Bot"
help_syntx = "Usage: `r!ping`"
class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    @commands.command()
    async def ping(self,ctx):
        embed = Embed(title="Ping",description=f'Pong! In {round(self.client.latency * 1000)}ms')
        await ctx.send(embed = embed)
        
def setup(client: commands.Bot):
    client.add_cog(Ping(client))