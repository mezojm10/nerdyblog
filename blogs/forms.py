from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title' : '', 'text' : ''}

class ContentForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title' : '', 'text' : ''}
        widget = {'text' : forms.Textarea(attrs={'cols' : 80})}
