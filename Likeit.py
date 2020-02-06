import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.YouLike

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.youtube.com/watch?v=OsOUcikyGRk&list=PLx8gFTVpu9vTOqUpUwG7tZQoiDihoGHsu',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#music-tab > div > div.list-wrap.scroll-wrap > ul > li.list.this-play > a:nth-child(2) > span.title.ellipsis
#music-tab > div > div.list-wrap.scroll-wrap > ul > li.list.this-play > a:nth-child(2) > span.artist.ellipsis
#video-title
#byline-containerz
musics = soup.select('#video-title')
number = 1
for music1 in musics:
    a_tag = music1.select_one()
    if a_tag is not None:
        title = a_tag.text
        singer = music1.select_one('#byline-containerz').text

        doc = {
            'number' : number,
            'title' : title.strip(),
            'singer' : singer
        }

        db.music.insert_one(doc)

        number += 1

