import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL )
parsed_data = response.json()

# JSON -> dict 데이터 변환
dummy_data = []
for i in range(10):
    company = parsed_data[i]['company']['name']
    lat = float(parsed_data[i]['address']['geo']['lat'])
    lng = float(parsed_data[i]['address']['geo']['lng'])
    name = parsed_data[i]['name']

    name_dict = {'company': company, 'lat': lat, 'lng': lng, 'name': name}
   
    if -80 < name_dict['lat'] < 80 and -80 < name_dict['lng'] < 80:
        dummy_data.append(name_dict)
    
print(dummy_data)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        if censorship(user):            
            censored_user_list[user['company']] = [user['name']]
    return censored_user_list


def censorship(list):
    if list['company'] in black_list:
        print(f'{list["company"]} 소속의 {list["name"]}은/는 등록할 수 없습니다.')
        return False
    else:
        print(f'이상없습니다.')
    return True 

print(create_user(dummy_data))