from django.db import models

# Create your models here.

class Weather(models.Model):
    #  남이 사용하기 쉽게 key 네임과 변수 이름 맞춰줌
    dt_txt = models.DateTimeField() # 관측시간
    temp = models.FloatField()      # 온도(기본값: 캘빈온도)
    feels_like = models.FloatField()# 체감온도(기본값:캘빈온도)
