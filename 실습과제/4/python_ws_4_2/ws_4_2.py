import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)
parsed_data = response.json()

# JSON -> dict 데이터 변환
dummy_data = []
for i in range(10):
    company = parsed_data[i]['company']['name']
    lat = float(parsed_data[i]['address']['geo']['lat'])
    lng = float(parsed_data[i]['address']['geo']['lng'])
    name = parsed_data[i]['name']

    name_dict = {'company': company, 'lat': lat, 'lng': lng, 'name': name}
    
for key in name_dict:
    if name_dict['lat'] <80 and name_dict['lng'] >-80:
        dummy_data.append(name_dict)
    
print(dummy_data)



