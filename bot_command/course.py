import discord
from discord.ext import commands
from discord.ext.buttons import Paginator
from bs4 import BeautifulSoup
from requests import get


class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass


class Course(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def course(self, ctx, *args):
        search = " ".join(args[:]).replace(' ', '+')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        data = []
        res = get(f"https://getfreecourses.co/?s={search}", headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.select('.post-title.post-url')
        no = 0
        for link in title:
            no += 1
            data.append({
                "no": no,
                "course": link['href'],
                "name": link.text.replace('\n', '').replace('/', '')
            })
        pager = Pag(
            entries=[
                f"```{i['no']}. {i['name']}```\n[Course Link]({i['course']})" for i in data],
            length=1,
            prefix="**GetFreeCourses.com**\n",
            suffix="")
        await pager.start(ctx)


def setup(client):
    client.add_cog(Course(client))
