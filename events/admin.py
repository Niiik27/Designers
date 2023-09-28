from django.contrib import admin
from .models import MyEvent
@admin.register(MyEvent)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title','date')
