from django.urls import path,include
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('accounts.urls')),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
