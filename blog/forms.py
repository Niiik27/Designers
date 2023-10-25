from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # image = forms.FileField(label="Изображение",widget=forms.FileInput(attrs={'class': 'txt-input','id':'img_file'}))
    # title = forms.CharField(label="Название",widget=forms.TextInput(attrs={'class': 'txt-input'}),help_text="Введите название")
    # desc = forms.CharField(label="Описание",widget=forms.Textarea(attrs={'class': 'txt-input'}))
    # date = forms.DateField(label="Дата",widget=forms.DateInput(attrs={'class': 'txt-input', 'type':'date'}))
    # url = forms.CharField(label="В сотрудничестве",widget=forms.TextInput(attrs={'class': 'txt-input'}))
    # id = forms.CharField(label="id_img", widget=forms.TextInput(attrs={'class': 'txt-input', 'hidden':"hidden"}))
    # title.label = ('port_label',)

    # def __init__(self, *args, **kwargs):
        # title = forms.CharField()
        # super().__init__(*args, **kwargs)
        # self.fields['title'].label_class = 'form-label'
        # self.fields['desc'].label_class = 'form-label'
        # self.fields['image'].label_class = 'form-label'
        # self.fields['date'].label_class = 'form-label'
        # self.fields['url'].label_class = 'form-label'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(dir(self.fields['title'].widget))
        # print(self)
        self.fields['title'].widget.attrs['class'] = 'form-text-input form'
        self.fields['desc'].widget.attrs['class'] = 'form-area-input'
        self.fields['image'].widget.attrs['class'] = 'form-text-input'
        self.fields['date'].widget.attrs['class'] = 'form-text-input'
        self.fields['url'].widget.attrs['class'] = 'form-text-input'

        # self.fields['title'].label.attrs['class'] = 'your-class-name'



        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'your-class-name'

        # for name, label in self.field_labels.items():
        #     self.fields[name].label_class = 'your-class'

        # for name, label in self.field_labels.items():
        #     self.fields[name].widget.attrs.update({'class': 'your-class'})

    class Meta:
        model = Article
        fields = '__all__'
        # fields = [
        #     'title',
        #     'desc',
        #     'image',
        #     'date',
        #     'url',
        # ]
        # widget = {
        #     'title': forms.TextInput(attrs={'class': 'text-input'}),
        #     'desc': forms.Textarea(attrs={'class': 'text-input'}),
        #     'image': forms.FileInput(attrs={'class': 'text-input'}),
        #     'date': forms.DateInput(attrs={'class': 'text-input'}),
        #     'url': forms.URLInput(attrs={'class': 'text-input'}),
        # }