
from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventsView, name=views.app_name),
]