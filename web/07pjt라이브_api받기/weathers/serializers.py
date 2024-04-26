from rest_framework import serializers 
from .models import Weather 


#  모델 시리얼라이즈에서 모델필드에 정의된 데이터만 변환: 모델시리얼라이저
#  필드에는 없어도 전부 변환: serializers.serializer
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
    