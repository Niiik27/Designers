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
            'sotial_vk',
            'sotial_ok',
            'sotial_inst',
            'sotial_tube',
            'username',
            'password',
            'about',
        ]