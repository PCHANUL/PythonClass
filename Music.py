import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.MusicRank1


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 1
for music in musics:
    a_tag = music.select_one('td.info > a')
    if a_tag is not None:
        title = a_tag.text
        singer = music.select_one('a.artist.ellipsis').text

        doc = {
            'rank' : rank,
            'title' : title.strip(),
            'singer' : singer,
        }
        # db.music.delete_one(doc)
        db.music.insert_one(doc)



        rank += 1

