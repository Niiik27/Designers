from django.urls import path
from . import views

urlpatterns = [
    path('', views.standardsView, name=views.app_name),
]