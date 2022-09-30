import discord
import os
from discord.ext.commands import CommandNotFound
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

#Setup
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="r!",intents = intents,help_command=None)

@client.command()
@commands.is_owner()
async def load(ctx,extension):
    try:
       client.load_extension(f"bot_command.{extension}")
       await ctx.send(f'`Loaded {extension} Successfully!`')
    except:
        await ctx.send("`Could'nt Load Extenstion`")
@client.command()
@commands.is_owner()
async def unload(ctx,extension):
    try:
         client.unload_extension(f"bot_command.{extension}")
         await ctx.send(f'Unloaded {extension} Successfully!')
    except:
        await ctx.send("`Could'nt Unload Extenstion")

#Add Commands
basepath = './bot_command'
for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        # skip directories
        continue
    else:
        if fname.endswith(".py"):
            client.load_extension(f"bot_command.{fname[:-3]}")

@client.event
async def on_ready():
    web = "https://RANDERBOT.samkhan4.repl.co"
    activity = discord.Activity(name="r!help",
                                type=discord.ActivityType.watching,
                                description=f"Our Website: {web}")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed(title="Oops !",color = discord.Color.red())
        embed.add_field(name="Command Not Found !",value ="Try Running **r!help** For Available Commands")
        await ctx.send(embed=embed)
    if isinstance(error,commands.MissingRequiredArgument):
       embed = discord.Embed(title="Oops !",color = discord.Color.red())
       embed.add_field(name="This Command Requires 1 Postional Arguement. ",value ="Try Running **r!help** For Detailed Information")
       await ctx.send(embed=embed)
    if isinstance(error,commands.BotMissingPermissions):
        embed = discord.Embed(title="Oops !",color = discord.Color.red())
        embed.add_field(name="I Don't Have Permisson To Execute Following Command. ",value ="Try Running **r!help** For Other Commands")
        await ctx.send(embed=embed)
    if isinstance(error,commands.NotOwner):
        embed = discord.Embed(title="Oops !",color = discord.Color.red())
        embed.add_field(name="You Don't Own This Bot Sorry",value ="Try Running **r!help** For Other Commands")
        await ctx.send(embed=embed)
    raise error

client.run(os.getenv("TOCKEN"))
