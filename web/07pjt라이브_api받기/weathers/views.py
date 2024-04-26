from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import requests 
from django.conf import settings
# Create your views here.
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.decorators import api_view

API_key = settings.WEATHER_API_KEY

def index(request):
    city_name='Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}'
    response = requests.get(url).json()

    # print(response)
    return JsonResponse(response)

# 원하는 데이터만 저장
def save_data(request):
    city_name='Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}'
    response = requests.get(url).json()


    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')

        # print(dt_txt)
        # print(temp)
        # print(feels_like)
        
        # 저장할 수 있도록 변환, 잘됐는지 is_valid, 저장 save 

        save_data = {
            'dt_txt' : dt_txt,
            'temp' : temp,
            'feels_like':feels_like,
        }
        # 변환하기 : 날씨 데이터를 json 파일로 변환 
        serializer = WeatherSerializer(data=save_data)
        # 유효성 검증도 시리얼라이저가 갖고있음 /raiseexception 트루하면 에러 리턴해줌
        if serializer.is_valid(raise_exception=True):
            serializer.save() 

    return JsonResponse({'message':'저장완료'}) # jsonresponse 는 장고에서 제공



@api_view(['GET'])
#  "restframework"의 api함수니까 json형태로 반환요구 
def list_data(request):
    weathers = Weather.objects.all() 
    serializers = WeatherSerializer(weathers,many=True)
    
    # rest framework 가 response 지원(장고아님) 
    #  -> 바로 하면 에러뜸, api함수 구현했으니 api view 데코레이터 해야함
    return Response(serializers.data)


@api_view(['GET '])
def hotweathers(reuest):
    weathers = Weather.objects.all() 

    hot_weathers = [] 
    for weather in weathers:
        celsius = round(Weather.temp - 273.15,2) # 섭씨 변환씩 
        if celsius >20:
            hot_weathers.append(weather)

    #  weathers = Weatehr.objects.filter(temp__gt=(20+273.15))
    # serlizers = weatherserizlizer(weatehrs, many=true)

    serializers = WeatherSerializer(hot_weathers, many=True)
    return Response(serializers.data)