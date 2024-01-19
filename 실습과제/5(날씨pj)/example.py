# 서버에서 데이터 가져오기
# https://fakestoreapi.com/carts

# 남들이 만든 코드 가져다 쓰기 : 라이브러리 
# 데이터 가져오는 라이브러리: requests
# 파이썬 패키지 관리: pip
    # pip install은 다운로드, #pip list는 목록확인
# 내 코드에 다른 패키지 추가

# pip 이용해서 requests 라이브러리를 설치한 것


import requests
import pprint

lat = 37.56
lon = 126.97
API_key = '87246d75e1ce26e1392a087b3d1d88c5'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'


data = requests.get(url).json() 
# get:url 에서 데이터 가져와라 
#.json: 내부 데이터를 딕셔너리 만들기 

pprint.pprint(data)
print(data['weather'][0]['description'])
print(data['weather'][0].get('description'))

# data['weather']
# data.get('weather') 차이