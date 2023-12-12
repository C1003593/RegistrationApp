from django import forms
from .models import Registration

class ModuleReg (forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['student', 'module']