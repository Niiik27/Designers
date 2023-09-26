
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileView, name=views.app_name),
]