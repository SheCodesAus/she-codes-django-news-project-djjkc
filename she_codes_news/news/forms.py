from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'style': 'width: 300px;'}), 
        'content':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your story here','style': 'width: 300px;'}),
        }