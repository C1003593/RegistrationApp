from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Module, Course, Registration, Teacher
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .forms import ModuleReg, ContactForm
from django.contrib import messages
from django.views.generic.edit import FormView



def home(request):

        course_list = {'courses': Course.objects.all(), 'title': 'Welcome'}
        return render(request, 'ModuleRegistrationSystem/home.html', course_list)

def about(request):

        return render(request, 'ModuleRegistrationSystem/about.html', {'title': 'About us'})

class ContactFormView(FormView):
        form_class = ContactForm
        template_name = 'ModuleRegistrationSystem/contact.html'

        def get_context_data(self, **kwargs: Any):
                context = super(ContactFormView, self).get_context_data(**kwargs)

                context.update({'title': 'Contact Us'})
                return context
        
        def form_valid(self, form):
                form.send_mail()
                messages.success(self.request, 'Successfully sent the enquiry')
                return super().form_valid(form)
        
        def form_invalid(self, form):
                messages.warning(self.request, 'Unable to send the enquiry')
                return super().form_invalid(form)
        
        def get_success_url(self):
                return self.request.path

def modules(request):
        
        module_list = {'modules': Module.objects.all(), 'title': 'List of modules'}
        return render(request, 'ModuleRegistrationSystem/modules.html', module_list)

def registrations(request):
        
        registrations_list = {'registrations': Registration.objects.all(), 'title': 'My Registrations'}
        return render(request, 'ModuleRegistrationSystem/my_registrations.html', registrations_list)

def teachers(request):

        teacher_list = {'teachers': Teacher.objects.all(), 'title': 'List of teachers'}
        return render(request, 'ModuleRegistrationSystem/teachers.html', teacher_list)

class TeacherListView(ListView):
        model = Teacher
        template_name = 'ModuleRegistrationSystem/teachers.html'
        context_object_name = 'teachers'
        ordering = ['Name']
        paginate_by = 3


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

def ModuleRegistration(request, pk):
        module = get_object_or_404(Module, code=pk)
        if request.method == "POST":
                form = ModuleReg(request.POST)
                if form.is_valid():
                        reg = form.save(commit=False)
                        reg.module = module
                        reg.student = request.user

                        reg.save()
                        messages.success(request, f"You have successfully registered for the module.")
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


        