from django import forms
from .models import appl

class appleForm(forms.ModelForm):
    class Meta:

        model = appl
        fields='__all__'

        widgets={
            'item':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Item Here'}),
            'price':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter Price Here'})
        }