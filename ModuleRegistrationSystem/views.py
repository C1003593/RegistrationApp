from django.shortcuts import render

def home(request):

        return render(request, 'ModuleRegistrationSystem/home.html')

def about_us(request):
        
        return render(request, 'ModuleRegistrationSystem/about.html')

def contact_us(request):
        
        return render(request, 'ModuleRegistrationSystem/contact.html')

def modules(request):
        
        return render(request, 'ModuleRegistrationSystem/modules.html')


# Create your views here.
