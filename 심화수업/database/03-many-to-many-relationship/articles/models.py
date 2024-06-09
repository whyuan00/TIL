from django.db import models
from django.conf import settings
# django에서는 User 모델을 '직접' 참조하지 않는다.
# from accounts.models import User


# Create your models here.
class Article(models.Model):

    #user모델 가져와서 세팅즈.quthusermodel 하면 user모델 참조해서 외래키
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 중개모델생성 
    # 단 위의 user.article_set과 매니저를 구분할수 없게됨
    # 유저가 작성한 게시글과 좋아요한 게시글 모두 user.article_set.all()되는문제
    # 따라서 related_name의 재설정 필요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
