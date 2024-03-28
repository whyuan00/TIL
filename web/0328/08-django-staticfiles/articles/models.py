from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 업로드투에 추가해서 미디어 폴더안에 추가경로 설정 
    image = models.ImageField(blank=True, upload_to='%Y%m/%d') # 빈이미지도 저장가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''
def articles_image_path(instance,filename):
    return f'images/{instance.user.username}/{filename}'
image = models.ImageField(blank=True,upload_to = articles_image_path)
'''