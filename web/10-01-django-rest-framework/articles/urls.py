from django.urls import path
from . import views

# app_name= 'articles' , name-'' 은 템플릿 렌더링안할거라 필요x
urlpatterns = [

    path('articles/',views.article_list),
    path('articles/<int:article_pk>/',views.article_detail),


]
