import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

# json을 python 타입으로 변환(문서를 받는게 아님, json자료형을 받는중)
result = response.json()

print(type(result)) # class 'list'
# pprint(result)
pprint(result[0])
# pprint(result[0].get('title'))
