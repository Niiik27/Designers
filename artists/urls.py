
from django.urls import path
from . import views

urlpatterns = [
    path('', views.artistsView, name='artists'),
]