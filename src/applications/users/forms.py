from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone', 'address', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = self.Meta.model.objects.create_user(
            email=self.cleaned_data.get("email"), 
            username=self.cleaned_data.get("username"), 
            password=self.clean_password2())
        user.phone = self.cleaned_data.get("phone")
        user.address = self.cleaned_data.get("address")
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'style': 'max-width: 300px;'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'style': 'max-width: 300px;'})
        self.fields['phone'].widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone', 'style': 'max-width: 300px;'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'style': 'max-width: 300px;'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'style': 'max-width: 300px;'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'style': 'max-width: 300px;'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'style': 'max-width: 300px;'})
        self.fields['phone'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone', 'style': 'max-width: 300px;'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'style': 'max-width: 300px;'})
