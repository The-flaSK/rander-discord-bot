import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import pytemperature

help_value = "Get Weather Info Of Required City or State"
help_syntax = "Usage: `r!weather` `<state/city>`"
class Weather(commands.Cog):
    def __init__(self,client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
       print("RANDER IS ONLINE !")
    #Commands
    @commands.command()
    async def weather(self,ctx,cityname):
     headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
     def weather(city):
         city = city.replace(" ", "+")
         res = requests.get(
        f'https://www.google.com/search?channel=nrow5&client=firefox-b-d&q=weather+of+{cityname}', headers=headers)
         soup = BeautifulSoup(res.text, 'html.parser')
         global location
         location = soup.select('#wob_loc')[0].getText().strip()
         global tiime
         tiime = soup.select('#wob_dts')[0].getText().strip()
         global info
         info = soup.select('#wob_dc')[0].getText().strip()
         global weatherz
         weatherz = int(soup.select('#wob_tm')[0].getText().strip())
         global imageofweatherz
         imageofweather = soup.select('#wob_tci')[0].attrs['src']
         imageofweatherz = 'https://'+imageofweather[2:]
     city = cityname
     city = city+" weather"
     weather(city)
     e = discord.Embed(title=f"Weather Of {location}",color = discord.Color.green())
     e.set_thumbnail(url=f"{imageofweatherz}")
     e.add_field(name=f"Time:",value=f"`{tiime}`",inline=False)
     e.add_field(name=f"Status:",value=f"`{info}`",inline=False)
     e.add_field(name=f"Temperature:",value=f"`{pytemperature.f2c(weatherz)} °C`",inline=False)
     e.set_footer(text="Requested By {} ".format(ctx.message.author.name))
     await ctx.send(embed=e)
 

def setup(client):
    client.add_cog(Weather(client))

