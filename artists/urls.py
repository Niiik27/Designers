
from django.urls import path
from . import views

urlpatterns = [
    path('', views.artistsView, name=views.app_name),
]