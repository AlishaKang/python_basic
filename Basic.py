# 1. apple / Apple
# 2. git add. / git add . 
# 3. message / massage

# 변수, variable
# 1. 숫자
dust = 10
# 2. 글자(string)
dust = '5'
# 3. 참/거짓(boolean)
dust = True # False

# ctrl + / 누르면 그 문장이 한 번에 주석처리가 된다.

# print(dust)

dust_list = [10, 20, 0, 50, 100]
# print(dust_list[3])
#0번부터 시작해서 50이 출력되어 나온다.

dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,
}
# print(dust_dict['부산'])



# 2. 조건
age = 10

if age > 20:
    print('성인입니다.')
elif age > 8:
    print('청소년입니다.')
else: 
    print('어린이입니다.')

dust = 30

# dust 150보다 크다면 -> 매우나쁨
# 80~149 -> 나쁨
# 30~79 -> 보통
# 0~29 -> 좋음

if dust >= 150:
    print('매우나쁨')
elif 80 <= dust < 150:
    print('좋음')
elif 30 <= dust  and dust < 80:
    print('보통')
else:
    print('좋음')



# 3. 반복
menus = ['짬뽕', '곱창', '마라탕', '도넛']

n = 0
while n < 4:
    print(menus[n])
    n = n + 1

for menu in menus: #범위, 수량 표시 for item in list
    print(menu)