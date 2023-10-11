from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    artwork = forms.FileField(widget=forms.FileInput(attrs={'class': 'button'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'txt-input'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={'class': 'txt-input'}))
    date = forms.CharField(widget=forms.TextInput(attrs={'class': 'txt-input'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'txt-input'}))
    class Meta:
        model = Artwork
        fields = [
            'image',
            'title',
            'desc',
            'date',
            'url',
        ]
