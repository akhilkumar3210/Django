from django import forms
from .models import *
class User(forms.Form):
    Name=forms.CharField()
    Age=forms.IntegerField()
    Email=forms.EmailField()
    
class Mform(forms.ModelForm):
    class Meta:
        model=Sample
        fields='__all__'