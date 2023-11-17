from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    DOB = forms.DateField(label = 'Date of birth', help_text = 'Your date of birth.' )
    Address = forms.CharField(label = 'Address')
    City = forms.CharField(label = 'City')
    Country = forms.CharField(label = 'Country')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'DOB', 'Address', 'City', 'Country', 'password1', 'password2']
