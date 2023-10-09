
from django.urls import path, include

from APP_NAMES import APP_NAMES
from . import views
from loginuser.views import profileView


urlpatterns = [
    path('', views.homeView, name=views.app_name),
]
