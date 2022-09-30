import discord
from discord.ext import commands
from traceback import format_exception
from discord.ext.buttons import Paginator
import io
import textwrap
import contextlib

whitelist = [813660012001624124]

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass
class Eval(commands.Cog):
    def __init__(self,client):
        self.client = client
        self._last_member = None
    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.is_owner()
    async def eval(self,ctx,*,code):
      if ctx.guild.id not in whitelist:
        def cleane_code(content):
             if content.startswith("```") and content.endswith("```"):
                return "/n".join(content.split("/n")[1:][:-3])
             return content
        code = cleane_code(code)
        local_variables = {
            "discord": discord,
            "commands": commands,
            "bot": self.client,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
        }
        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code,'    ')}",local_variables
                )
                obj = await local_variables['func']()
                result = f"{stdout.getvalue()}\n--{obj}\n"
        except Exception as e:
            result = "".join(format_exception(e,e,e.__traceback__))
        
        pager = Pag(
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```")
        await pager.start(ctx)
      else:
          await ctx.send("`Restricted Here!`")
          
def setup(client):
    client.add_cog(Eval(client))