from django import forms
from .models import Media 

class MediaForm(forms.Form):
    class Meta:
        model = Media
        fields = ['title', 'poster', 'year']