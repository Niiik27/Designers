
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contestsView, name=views.app_name),
]