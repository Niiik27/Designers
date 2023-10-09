from django.apps import AppConfig
from APP_NAMES import APP_NAMES

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = APP_NAMES.HOME
