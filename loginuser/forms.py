from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'photo_url',
            'image',
            'firstname',
            'lastname',
            'birth',
            'e_mail',
            'phone',
            'purpose',
            'social_vk',
            'social_ok',
            'social_inst',
            'social_tube',
            'username',
            'password',
            'about',
        ]