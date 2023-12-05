from django.shortcuts import render, redirect
from .models import Module, Course
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


class ModuleListView(ListView):
        model = Module
        template_name = 'ModuleRegistrationSystem/modules.html'
        context_object_name = 'modules'
        ordering = ['code']
        paginate_by = 3

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
        