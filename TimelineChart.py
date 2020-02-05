import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.MusicRankTimeline



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

baseUrl = 'https://www.genie.co.kr/chart/musicHistory?year={}'
n = 2019
for n in range (10):
    data = requests.get(baseUrl.format(n-1), headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    musics = soup.select('#body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr')
#body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

    rank = 1
    for  in musics:
        a_tag = n.select_one('a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = n.select_one('a.artist.ellipsis').text

            doc = {
            'rank' : rank,
            'title' : title.strip(),
            'singer' : singer,
            }

            # db.In2018.delete_one(doc)
            db.n.insert_one(doc)
            rank += 1


