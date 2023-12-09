from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Module, Course, Registration
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

def home(request):

        course_list = {'courses': Course.objects.all(), 'title': 'Welcome'}
        return render(request, 'ModuleRegistrationSystem/home.html', course_list)

def about(request):

        return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About us'})

def contact(request):
        
        return render(request, 'ModuleRegistrationSystem/contact.html', {'title': 'Contact us'})

def modules(request):
        
        module_list = {'modules': Module.objects.all(), 'title': 'List of modules'}
        return render(request, 'ModuleRegistrationSystem/modules.html', module_list)

def registrations(request):
        
        registrations_list = {'registrations': Registration.objects.all(), 'title': 'My Registrations'}
        return render(request, 'ModuleRegistrationSystem/my_registrations.html', registrations_list)

                

class ModuleListView(ListView):
        model = Module
        template_name = 'ModuleRegistrationSystem/modules.html'
        context_object_name = 'modules'
        ordering = ['code']
        paginate_by = 3

class RegistrationView(ListView):
        model = Registration
        template_name = 'ModuleRegistrationSystem/my_registrations.html'
        context_object_name = 'registrations'
        paginate_by = 3

        def get_queryset(self):
                user=get_object_or_404(User, username=self.kwargs.get('username'))
                return Registration.objects.filter(student=user).order_by('dateOfRegistration')



class ModuleDetailView(DetailView):
        model = Module

class CourseDetailView(DetailView):
        model = Course

class ModuleCreateView(CreateView):
        model = Module
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'coursesAllowedToRegister']

class ModuleUpdateView(UpdateView):
        model = Module
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'coursesAllowedToRegister']

class ModuleDeleteView(DeleteView):
        model = Module
        success_url = '/modules'
        