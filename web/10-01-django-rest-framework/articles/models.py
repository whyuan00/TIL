from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#serilalization: 직렬화
#데이터구조나 객체상태를 재구성가능한 포맷으로변환하는과정