from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # following 구현 위한 참조 역참조관계 생각해보기
    # 참조가 following 역참조가 follower (나를 기준으로 둘때)
    # 일방적인 follow 구현할거라서 대칭=False 구현
    followings = models.ManyToManyField('self', symmetrical=False, related_name= 'followers') 
    # 이름 안바꿔주면 역참조할떄 user2.User_set.all()이 됨 
    
