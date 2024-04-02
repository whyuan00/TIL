from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('',views.index,name='index'),

    # variable bouting? 
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/',views.create,name='create'),

    # 수정과 삭제의 전제조건: 조회가 먼저 ->url의 pk가 필수
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    
]
