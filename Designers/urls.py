"""
URL configuration for Designers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from APP_NAMES import APP_NAMES
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(f'{APP_NAMES.HOME}.urls')),
    path(f'{APP_NAMES.BLOG}/', include(f'{APP_NAMES.BLOG}.urls')),
    path(f'{APP_NAMES.PORTFOLIO}/', include(f'{APP_NAMES.PORTFOLIO}.urls')),
    path(f'{APP_NAMES.USER_MESSAGES}/', include(f'{APP_NAMES.USER_MESSAGES}.urls')),
    path(f'{APP_NAMES.ARTISTS}/', include(f'{APP_NAMES.ARTISTS}.urls')),
    path(f'{APP_NAMES.STANDARDS}/', include(f'{APP_NAMES.STANDARDS}.urls')),
    path(f'{APP_NAMES.EVENTS}/', include(f'{APP_NAMES.EVENTS}.urls')),
    path(f'{APP_NAMES.PARTNERS}/', include(f'{APP_NAMES.PARTNERS}.urls')),
    path(f'{APP_NAMES.CONTESTS}/', include(f'{APP_NAMES.CONTESTS}.urls')),
    path(f'{APP_NAMES.LOGIN_USER}/', include(f'{APP_NAMES.LOGIN_USER}.urls')),
    path(f'{APP_NAMES.ISSUES}/', include(f'{APP_NAMES.ISSUES}.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
