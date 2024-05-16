from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # 이 주소를 제일 위로 보내면 모든 url이 username 으로감.
    #따라서 앞에 주소 더 붙여줌
    path('profile/<str:username>/',views.profile, name='profile'),
    # 팔로우 요청할떄 , userpk는 상대방조회목적
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    

]
