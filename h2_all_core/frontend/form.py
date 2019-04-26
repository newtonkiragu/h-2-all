from .models import Price, Borehole
from django import forms

class NewPriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['per_litre', 'name']
        exclude = ['user']

class NewBoreholeForm(forms.ModelForm):
    class Meta:
        model = Borehole
        fields = ['phone_number', 'location', 'price']
        exclude = ['user']