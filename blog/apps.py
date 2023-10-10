from django.apps import AppConfig
from APP_NAMES import APP_NAMES,VERBOSE_APP_NAMES

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = APP_NAMES.BLOG
    verbose_name = VERBOSE_APP_NAMES.BLOG
