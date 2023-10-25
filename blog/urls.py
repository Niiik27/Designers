
from django.urls import path
from . import views
from APP_NAMES import APP_NAMES,VERBOSE_APP_NAMES
urlpatterns = [
    path('', views.blogView, name=views.app_name),
    path('<int:article_id>/', views.detailView, name=APP_NAMES.ARTICLE),
    path(f'{APP_NAMES.NEWARTICLE}/', views.newArticleView, name=APP_NAMES.NEWARTICLE),
]

