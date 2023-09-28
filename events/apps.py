from django.apps import AppConfig
# from . views import app_name,verbose_app_name

class MyEventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
    verbose_name = 'События'
