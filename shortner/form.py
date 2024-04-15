from django import forms
from .models import URL

class formInput(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['link','short_link']

