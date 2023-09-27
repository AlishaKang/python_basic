##미세먼지 농도와 상태 알려주기

import requests
from pprint import pprint #깔끔하게 정렬해서 보여줌

URL = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2B58fRxySTvs0PfFQUY4WIxmfUdNzO2PRCGrFR%2BwurNXadOEb4nRyU4TfZFft%2FX7IOwZchblSbWUzs2S9mm1q2Q%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

res = requests.get(URL)

data = res.json()

items = data['response']['body']['items']

for item in items:
    if item['stationName'] == '강남구':
        pprint(item['pm10Value'])