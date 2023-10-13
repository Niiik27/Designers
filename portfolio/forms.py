from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    image = forms.FileField(label="Изображение",widget=forms.FileInput(attrs={'class': 'button'}))
    title = forms.CharField(label="Название",widget=forms.TextInput(attrs={'class': 'txt-input'}),help_text="Введите название")
    desc = forms.CharField(label="Описание",widget=forms.Textarea(attrs={'class': 'txt-input'}))
    date = forms.CharField(label="Дата",widget=forms.TextInput(attrs={'class': 'txt-input'}))
    url = forms.CharField(label="В сотрудничестве",widget=forms.TextInput(attrs={'class': 'txt-input'}))
    # title.label = ('port_label',)
    class Meta:
        model = Artwork
        fields = [
            'image',
            'title',
            'desc',
            'date',
            'url',
        ]
