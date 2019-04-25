from .models import Price
from django import forms

class NewPriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['per_litre', 'name']
        exclude = ['user']
