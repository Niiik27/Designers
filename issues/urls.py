
from django.urls import path
from . import views

urlpatterns = [
    path('', views.issuesView, name=views.app_name),
]