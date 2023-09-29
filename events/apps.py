from django.apps import AppConfig
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES

class MyEventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = APP_NAMES.EVENTS
    verbose_name = VERBOSE_APP_NAMES.EVENTS
