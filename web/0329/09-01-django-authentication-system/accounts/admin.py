from django.contrib import admin

# Register your models here.
# 새로운 user모델을 admin에 등록해야함 
from django.contrib.auth.admin import UserAdmin
from .models import User 

admin.site.register(User, UserAdmin)