import discord 
from discord.ext import commands
import typing


help_box  = {
    "ping":{
        "syntax":"`r!ping`",
        "usage":"`Get Bot Latency`"
    },
    "info":
        {
            "syntax":"`r!info` `<item>`",
            "usage":"`Get Info Of Something From Wikipedeia !` "
        },
    "month":{
        "syntax":"`r!month` `<year>` `<month>`",
        "usage":"`Get Dates And Days Of A Required Month From Any Year`"
    },
    "quote":{
        "syntax":"`r!quote`",
        "usage":"`Get A Random  Motivating Quote !`"
    },
    "fact":{
        "syntax":"`r!fact`",
        "usage":"`Get A Random Never Heard Fact !`"
    },
    "weather":{
        "syntax":"`r!weather` `<city/town>`",
        "usage":"`Get Weather Of Required City Or Town !`"
    },
    "course":{
        "syntax":"`r!course` `<coursename>`",
        "usage":"`Get Udemy Courses For Free` "
    }
}


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    @commands.command()
    async def help(self,ctx,cmd: typing.Optional[str]):
        not_commands = ["help","eval","load","unload"]
        yes_commands = [cmd.name for cmd in self.client.commands]
        if not cmd:
            help_embed = discord.Embed(title="RANDER Help Box",description="Our Bot Prefix Is `r!`",color=discord.Color.green())
            for command in self.client.commands:
                if command.name in not_commands:
                    pass
                else:
                    help_embed.add_field(name=command.name.capitalize(),value=help_box[command.name]["usage"],inline=False)
            await ctx.channel.send(embed = help_embed)     
        else:
            conv_cmd = cmd.lower()
            if conv_cmd in not_commands:
                ncmd_embed = discord.Embed(title="Not Command Found",description="Try running `r!help`",color=discord.Color.orange())
                await ctx.channel.send(embed = ncmd_embed)
            else:
                if conv_cmd in yes_commands:
                    cmd_embed = discord.Embed(title=cmd.capitalize(),description=f"Use:{help_box[conv_cmd]['usage']}\nUsage:{help_box[conv_cmd]['syntax']}",color=discord.Color.green())
                    await ctx.channel.send(embed = cmd_embed)
                else:
                    not_cmd_embed = discord.Embed(title="Not Command Found",description="Try running `r!help`",color=discord.Color.orange())
                    await ctx.channel.send(embed = not_cmd_embed)

def setup(client):
    client.add_cog(Help(client))
