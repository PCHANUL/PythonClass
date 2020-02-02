import requests

data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
datajson = data.json()
# print(datajson)

gus = datajson['RealtimeCityAir']['row']
# print(gus)

for gu in gus :
    if gu['IDEX_MVL'] < 80:
        print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

def get_mise(gu_name):
    for gu in gus:
        if gu['MSRSTE_NM'] == gu_name:
            return gu['INDEX_MVL']
    return '일치하는 구 이름이 없습니다.'

print(get_mise('종로구'))
