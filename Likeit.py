import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

for a in range (1) :
client = MongoClient('localhost',27017)
db = client.Genre
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
genre_url = 'https://www.genie.co.kr/chart/genre?ditc=D&ymd=20200206&genrecode={}&pg='

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0100')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.K_POP.insert_one(doc)
            rank += 1


rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0200')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.POP.insert_one(doc)
            rank += 1

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0300')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.OST.insert_one(doc)
            rank += 1

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0400')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.J_POP.insert_one(doc)
            rank += 1


rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0500')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.JAZZ.insert_one(doc)
            rank += 1

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0600')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.CLASSIC.insert_one(doc)
            rank += 1

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0700')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.NEWAGE.insert_one(doc)
            rank += 1

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0800')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.CCM.insert_one(doc)
            rank += 1

rank = 1
for n in range (2) :
    genre_url = genre_url.format('M0900')
    base_url = genre_url + '{}'
    url = base_url.format(n+1)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for Music in musics:
        a_tag = Music.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
            title = a_tag.text
            singer = Music.select_one('a.artist.ellipsis').text
            album = Music.select_one('a.albumtitle.ellipsis').text

            doc = {
                'Rank' : rank,
                'Title' : title,
                'Singer' : singer,
                'Album' : album
            }

            # db.K_pop.delete_one(doc)
            db.KIDSONG.insert_one(doc)
            rank += 1

