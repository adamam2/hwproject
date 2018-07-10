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
    long_description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': "Write a long description...",
            'size': 7
        }
    ))
    
    class Meta:
        model = Concept
        fields = ('name', 'description', 'area', 'long_description')
