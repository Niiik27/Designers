from django.apps import AppConfig
from . views import app_name,verbose_name

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = app_name
    verbose_name = verbose_name
