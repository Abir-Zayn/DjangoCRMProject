from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record 


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__' 
