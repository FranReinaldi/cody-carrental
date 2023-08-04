from django import forms
from .models import Manufacturer, Car

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['manufacturer', 'model','year']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['manufacturer'].widget = forms.Select(choices=self.fields['manufacturer'].choices, attrs={'class': 'form-control'})
        self.fields['model'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['year'].widget = forms.TextInput(attrs={'class': 'form-control'})