
from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventsView, name=views.app_name),
    path('<int:event_id>/', views.detailView, name='event'),
]