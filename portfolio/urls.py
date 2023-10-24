
from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/', views.portfolioView, name=views.app_name),
]
