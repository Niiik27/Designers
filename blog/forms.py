from django import forms
from django.utils.html import format_html

from .models import Article
from django.forms import BaseForm
class ArticleForm(forms.ModelForm):
    self_defs = ['add_error',
     'add_initial_prefix',
     'add_prefix',
     'as_div',
     'as_p',
     'as_table',
     'as_ul',
     'auto_id',
     'base_fields',
     'changed_data',
     'clean',
     'data',
     'declared_fields',
     'default_renderer',
     'empty_permitted',
     'error_class',
     'errors',
     'field_order',
     'fields',
     'files',
     'full_clean',
     'get_context',
     'get_initial_for_field',
     'has_changed',
     'has_error',
     'hidden_fields',
     'initial',
     'instance',
     'is_bound',
     'is_multipart',
     'is_valid',
     'label_suffix',
     'media',
     'non_field_errors',
     'order_fields',
     'prefix',
     'render',
     'renderer',
     'save',
     'template_name',
     'template_name_div',
     'template_name_label',
     'template_name_p',
     'template_name_table',
     'template_name_ul',
     'use_required_attribute',
     'validate_unique',
     'visible_fields']

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


        print(dir(self.fields['date'].widget.attrs))
        print(self.fields['date'].widget.attrs)
        # print(dir(self))
        self.fields['title'].widget.attrs['class'] = 'form-text-input form'
        self.fields['desc'].widget.attrs['class'] = 'form-area-input'
        self.fields['image'].widget.attrs['class'] = 'form-img-input'

        self.fields['date'].widget.attrs['class'] = 'form-text-input'
        # self.fields['date'].widget.attrs.pop('type')
        self.fields['date'].widget.attrs['type'] = 'date'
        self.fields['date'].widget.attrs.update({'type' : 'date'})
        self.fields['url'].widget.attrs['class'] = 'form-text-input'


        # self.fields['title'].label_tag(attrs={'class':'bla'})
        # self.fields['title'].label.attrs['class'] = 'your-class-name'



        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'your-class-name'

        # for name, label in self.field_labels.items():
        #     self.fields[name].label_class = 'your-class'

        # for name, label in self.field_labels.items():
        #     self.fields[name].widget.attrs.update({'class': 'your-class'})
    # def label_tag(self):
    #     return self.render(self.template_name_p)
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

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