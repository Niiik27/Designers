
from django.urls import path

from APP_NAMES import APP_NAMES
from . import views

urlpatterns = [
    path('', views.artistsView, name=views.app_name),
    path('<str:username>/', views.artis, name=APP_NAMES.ARTISTS),
]