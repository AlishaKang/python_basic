numbers = [1, 2, 3, 4, 5]

#max([1, 2, 3, 4, 5])
max_num = max(numbers)

# print(max_num)

####

import random
random_number = random.randint(1, 100)
# print(random_number)

####

menus = ['김밥', '라면', '만두'] #key = value
random_number = random.randint(0, 2) #randomint의 줄임말 randint
# print(menus[random_number])

menu = random.choice(menus) #복원 숫자 선택, 중복 숫자 니올 수도 있음
# print(menu)

####

numbers = range(1, 46) #1이상 46미만
lucky_number = random.sample(numbers, 6) #비복원 숫자 선택
# print(sorted(lucky_number)) #오름차순 정렬

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

# pip install requests 먼저 해야함
import requests

res = requests.get(URL)

#data = res.text #문자
data = res.json() #자료형

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)
print(data['drwNoDate'])

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number)) #교집합 출력, 교집합이 없으면 set()출력


