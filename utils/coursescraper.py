from bs4 import BeautifulSoup
from requests import get

def get_course(args):
    search = "+".join(args[:]).replace(' ','+')
    data = []
    res = get(f"https://getfreecourses.co/?s={search}")
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('.post-title.post-url')
    for link in title:
        data.append({
            "course":link['href'],
            "name":link.text.replace('\n','').replace('/','')
        })
    return data 