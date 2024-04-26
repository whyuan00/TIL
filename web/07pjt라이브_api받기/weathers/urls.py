"""
URL configuration for examplepjt project.

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
from django.urls import path,include 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('save_data/',views.save_data ,name='save_data'),
    path('list_data/', views.list_data, name='list_data'),
    path('hotweathers/', views.hotweathers, name='hotweathers'),
]
