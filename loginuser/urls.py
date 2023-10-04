
from django.urls import path, include
from . import views
from APP_NAMES import APP_NAMES

urlpatterns = [
    path('', views.loginuserView, name=APP_NAMES.LOGIN_USER),
    path(f'{APP_NAMES.LOGOUT_USER}/', views.logoutuserView, name=APP_NAMES.LOGOUT_USER),
    path(f'{APP_NAMES.REG_USER}/', views.reguserView, name=APP_NAMES.REG_USER),
    path(f'{APP_NAMES.USER_PROFILE}/', include(f'{APP_NAMES.USER_PROFILE}.urls')),
]