import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

help_value = "Get Info Of SomeThing"
help_syntax = "Usage: `r!info` `<item>`\nNote: Use `_` For Multi Arguements"
class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    @commands.command()
    async def info(self,ctx,item):
       searchitem = item
       def imageget(itemz):
            res = requests.get(f'https://www.google.com/search?q={itemz}_image&client=firefox-b-d&channel=nrow5&sxsrf=AOaemvIUCv4OMQlWyeUKmBfTXWiRrYgXkA:1642743132241&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj8j-qGj8L1AhV0wjgGHQmHBsoQ_AUoA3oECAIQBQ')
            soup = BeautifulSoup(res.text, 'html.parser')
            global imagelink
            imagelink = soup.select('.yWs4tf')[0]['src']
       imageget(searchitem)
       headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
       res = requests.get(f'https://en.wikipedia.org/w/index.php?search={item}&title=Special:Search&profile=advanced&fulltext=1&ns0=1',headers=headers)
       soupe = BeautifulSoup(res.text, 'html.parser')
       global heading
       try:  
             global searchresult
             searchresult = []
             for result in range(5):
                 heading = soupe.select('.searchresult')[result].getText()
                 searchresult.append(heading)
             heading = soupe.select('.searchresult')[0].getText()
             global heading2 
             heading2 = soupe.select('.searchresult')[1].getText()
             global heading3
             heading3 = soupe.select('.searchresult')[2]  .getText()
             global heading4
             heading4 = soupe.select('.searchresult')[3].getText()
             global heading5
             heading5 = soupe.select('.searchresult')[4].getText()
             global link
             link = soupe.select('.mw-search-result-heading')[0].contents[0]['href']
             global hoding
             hoding = soupe.select('.mw-search-result-heading')[0].contents[0]['title']
             global hoding2
             hoding2 = soupe.select ('.mw-search-result-heading')[1].contents[0]['title']
             global hoding3
             hoding3 = soupe.select('.mw-search-result-heading')[2].contents[0]['title']
             global hoding4
             hoding4 = soupe.select('.mw-search-result-heading')[3].contents[0]['title']
             global hoding5
             hoding5 = soupe.select('.mw-search-result-heading')[4].contents[0]['title']
             embed = discord.Embed(title=f"Info for {item.capitalize()}",color = discord.Color.green())
             embed2 = discord.Embed(title=f"Extra Info For {item.capitalize()}",color = discord.Color.green())
             embed.set_thumbnail(
            url=f"{imagelink}"
        )
             embed.add_field(name=hoding,value=heading,inline=False)
             embed2.add_field(name=hoding2.capitalize(),value=heading2,inline=False)
             embed2.add_field(name=hoding3.capitalize(),value=heading3,inline=False)
             embed2.add_field(name=hoding4.capitalize(),value=heading4,inline=False)
             embed.set_footer(text="Requested By {}\nReact Below To Get Realed Items".format(ctx.message.author.name))
             embed2.set_footer(text="Requested By {}".format(ctx.message.author.name))
             embed2.add_field(name=hoding5.capitalize(),value=heading5,inline=False)
             embed.add_field(name="Get More Info",value=f'[Get Full Info](https://en.wikipedia.org/{link})',inline=False)
             wikinfo = await ctx.send(embed=embed)
             await wikinfo.add_reaction('➕')
             def check_reaction(reaction, reaction_user):
                   return reaction.emoji == "➕" and reaction_user == ctx.author and reaction.message == wikinfo
             while True:
                 try:
                      reaction, user = await self.client.wait_for("reaction_add", timeout=10, check=check_reaction)
                      await ctx.send(embed=embed2)
                      break
                 except:
                      pass

       except IndexError:
         embod = discord.Embed(title=f"No Info Found for {item.capitalize()}",color = discord.Color.red())
         await ctx.send(embed=embod)
         
def setup(client):
    client.add_cog(Info(client))
