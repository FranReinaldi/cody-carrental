from django import forms
from .models import Manufacturer, Car, Rental

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['manufacturer', 'model','year','daily_price']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['manufacturer'].widget = forms.Select(choices=self.fields['manufacturer'].choices, attrs={'class': 'form-control'})
        self.fields['model'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['year'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['daily_price'].widget = forms.TextInput(attrs={'class': 'form-control'})

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'customer', 'start_date', 'end_date','calification']

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['car'].widget = forms.Select(choices=self.fields['car'].choices, attrs={'class': 'form-control'})
        self.fields['customer'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['start_date'].widget = forms.DateInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Select a date',
                                                                'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Select a date',
                                                                'type': 'date'})
        self.fields['calification'].widget = forms.TextInput(attrs={'class': 'form-control'})