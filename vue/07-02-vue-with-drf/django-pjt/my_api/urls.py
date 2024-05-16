"""
URL configuration for my_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    # 새로추가한 장고 rest_auth가 제공하는 앱으로 사용 
    path('accounts/', include('dj_rest_auth.urls')),
    # 등록기능 추가설정 -> 패키지 추가설치, app등록, url등록, migrate 
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),


]
    # 0fb619fbd4cfc5e4c8f49b09b537da89283ee2ce  
    
    # Using the URLconf defined in my_api.urls, Django tried these URL patterns, in this order:

    # admin/
    # api/v1/
    # accounts/ password/reset/ [name='rest_password_reset']
    # accounts/ password/reset/confirm/ [name='rest_password_reset_confirm']
    # accounts/ login/ [name='rest_login']
    # accounts/ logout/ [name='rest_logout']
    # accounts/ user/ [name='rest_user_details']
    # accounts/ password/change/ [name='rest_password_change']
    # accounts/signup/

    
