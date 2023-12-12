from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Module, Course, Registration
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .forms import ModuleReg
from django.contrib import messages



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
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'courses_Allowed_To_Register']

class ModuleUpdateView(UpdateView):
        model = Module
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'courses_Allowed_To_Register']

class ModuleDeleteView(DeleteView):
        model = Module
        success_url = '/modules'
"""
class ModuleRegistration(CreateView):
        model = Registration
        fields = ['module']
        def form_valid(self, form):
                form.instance.student = self.request.user
                return super().form_valid(form)
        success_url = '/modules'
"""

def ModuleRegi(request, pk):
        module = get_object_or_404(Module, code=pk)
        if request.method == "POST":
                form = ModuleReg(request.POST)
                if form.is_valid():
                        reg = form.save(commit=False)
                        reg.module = module
                        reg.student = request.user

                        reg.save()
                        messages.success(request, f"You have successfully registered from the module.")
                        return redirect('ModuleRegistrationSystem:modules')
                else:
                        messages.warning(request, f"You are already registered for this module.")
                        print(f"Form Errors: {form.errors}")
        else:
                form = ModuleReg()
        return redirect('ModuleRegistrationSystem:modules')

        
class ModuleDeregistration(SuccessMessageMixin, DeleteView):
        model = Registration
        success_message = "You have successfully deregistered from the module."

        def get_success_url(self):
                return reverse('ModuleRegistrationSystem:registrations', kwargs={'username': self.request.user.username})


        