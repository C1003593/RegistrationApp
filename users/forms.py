from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import studentAccount

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']
    
class studentAccountUpdateForm(forms.ModelForm):
    DOB = forms.DateField(help_text = 'Enter in the format: yyyy-mm-dd')
    class Meta:
        model = studentAccount
        fields = ['DOB', 'Address', 'City', 'Country', 'Course', 'image']