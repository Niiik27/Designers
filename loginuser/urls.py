
from django.urls import path
from . import views
from APP_NAMES import APP_NAMES

urlpatterns = [
    path('', views.loginuserView, name=APP_NAMES.LOGIN_USER),
]