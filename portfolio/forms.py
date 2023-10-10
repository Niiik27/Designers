from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = [
            'user',
            'title',
            'desc',
            'date',
            'url',
        ]