
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView, name=views.app_name),
    path('<str:username>/', views.profileView, name='username'),
]
