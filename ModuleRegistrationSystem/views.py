from django.shortcuts import render

def home(request):

        return render(request, 'ModuleRegistrationSystem/home.html', {'title': 'Welcome'})

def about(request):
        
        return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About us'})

def contact(request):
        
        return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact us'})

def modules(request):
        
        return render(request, 'ModuleRegistrationSystem/modules.html', {'title': 'Module list'})


# Create your views here.
