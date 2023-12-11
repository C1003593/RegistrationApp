from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ModuleRegistrationSystem.models import Course
from .models import studentAccount

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'course']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']
    
class studentAccountUpdateForm(forms.ModelForm):
    DOB = forms.DateField(help_text = 'Enter in the format: yyyy-mm-dd')
    class Meta:
        model = studentAccount
        fields = ['DOB', 'Address', 'City', 'Country', 'image']
        