from django.shortcuts import render
from .models import Module

def home(request):

        return render(request, 'ModuleRegistrationSystem/home.html', {'title': 'Welcome'})

def about(request):
        
        return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About us'})

def contact(request):
        
        return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact us'})

def modules(request):
        
        module_list = {'modules': Module.objects.all(), 'title': 'List of modules'}
        return render(request, 'ModuleRegistrationSystem/modules.html', module_list)


# Create your views here.
