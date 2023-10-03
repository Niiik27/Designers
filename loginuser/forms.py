from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'image_profile',
            'firstname',
            'secondname',
            'birthday',
            'about',
            'confirm_document'
        ]