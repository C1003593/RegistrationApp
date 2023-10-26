from django.shortcuts import render
from django.http import HttpResponse

def home(request):

        return HttpResponse('<h1>Welcome to Sheffield Hallam University</h1>')

def about_us(request):
        
        return HttpResponse('<h1>About the University</h1>')

def contact_us(request):
        
        return HttpResponse('<h1>Where to contact us</h1>')

def modules(request):
        
        return HttpResponse('<h1>Modules on offer</h1>')


# Create your views here.
