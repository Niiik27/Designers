
from django.urls import path
from . import views


urlpatterns = [
    path('', views.partnersView, name=views.app_name),
]