
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogView, name=views.app_name),
    path('<int:article_id>/', views.detailView, name='detail'),
]
