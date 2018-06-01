from django.forms import ModelForm
from collection.models import Concept

class ConceptForm(ModelForm):
    class Meta:
        model = Concept
        fields = ('name', 'description', 'area',)