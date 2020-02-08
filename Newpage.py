import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200208'




# range 파라미터
# range(stop)
# range(start, stop)
# range(start, stop, step)

pageNum = 1

for page in range (1,5):
    params = {'pg':pageNum}
    data = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # select를 이용해서, tr들을 불러오기
    geniecharts = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    pageNum += 1




    # movies (tr들) 의 반복문을 돌리기
    # rank = 1
    for geniechart in geniecharts:
        # movie 안에 a 가 있으면,
        a_tag = geniechart.select_one('td.info > a')
        rank = geniechart.select_one('td.number').contents[0].strip()
        artist = geniechart.select_one('a.artist.ellipsis').text
        # print('a_tag')
        if a_tag is not None:
            # songname = str.strip(a_tag.text)
            songname = a_tag.text.strip()
            doc = {
                'rank' : rank,
                'SongName' : songname,
                'Artist' : artist

            }
            db.geniechart.insert_one(doc)

            print(rank, songname)

