from django.contrib import admin
from .models import UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','firstname','lastname','birth')
    search_field = ('username','firstname','lastname','birth')
