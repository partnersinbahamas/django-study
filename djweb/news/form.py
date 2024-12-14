from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'desctiption', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form_item form-control',
                'placeholder': 'Name',
            }),
            'desctiption': TextInput(attrs={
                'class': 'form_item form-control',
                'placeholder': 'Desctiption',
            }),
            'text': Textarea(attrs={
                'class': 'form_item form-control',
                'placeholder': 'State',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form_item form-control',
                'placeholder': 'Date',
                'type': 'date'
            }),
        }