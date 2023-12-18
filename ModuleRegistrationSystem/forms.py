from django import forms
from .models import Registration
from django.core.mail import send_mail




class ModuleReg (forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['student', 'module']

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField()
    subject = forms.CharField(max_length = 100)
    enquiry = forms.CharField(widget = forms.Textarea)

    def send_mail(self):
        send_mail(self.cleaned_data.get('subject') + ', sent on behalf of ' + self.cleaned_data.get('name'), self.cleaned_data.get('enquiry'), self.cleaned_data.get('email'), ['C1003593@my.shu.ac.uk'])