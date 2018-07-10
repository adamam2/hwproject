from django import forms
from .models import Concept
from django.forms import ModelForm
from collection.models import Concept

class ConceptForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Add a name..."
        }
    ))
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Write a short description..."
        }
    ))
    
    class Meta:
        model = Concept
        fields = ('name', 'description', 'area', 'long_description')
