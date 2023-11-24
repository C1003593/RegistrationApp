from django.shortcuts import render, redirect
from .models import Module
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User

def home(request):

        return render(request, 'ModuleRegistrationSystem/home.html', {'title': 'Welcome'})

def about(request):
        
        return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About us'})

def contact(request):
        
        return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact us'})

def modules(request):
        
        module_list = {'modules': Module.objects.all(), 'title': 'List of modules'}
        return render(request, 'ModuleRegistrationSystem/modules.html', module_list)

class PostListView(ListView):
        model = Module
        template_name = 'ModuleRegistrationSystem/modules.html'
        context_object_name = 'modules'
        ordering = ['code']

class PostDetailView(DetailView):
        model = Module


class PostCreateView(CreateView):
        model = Module
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'coursesAllowedToRegister']
        