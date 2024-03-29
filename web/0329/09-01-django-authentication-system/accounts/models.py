from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
#관리자권한겸 user모델 구현하는 클래스 
class User(AbstractUser):
    pass 