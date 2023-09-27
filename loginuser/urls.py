
from django.urls import path
from . import views


urlpatterns = [
    path('', views.reguserView, name=views.app_name),
]