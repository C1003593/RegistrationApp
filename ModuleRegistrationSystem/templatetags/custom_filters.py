from django import template
from ModuleRegistrationSystem.models import Registration, Module
from django.contrib.auth.models import User
from users.models import studentAccount

register = template.Library()

@register.filter(name = 'if_registered')
def if_registered(student, module):
    return Registration.objects.filter(student = student, module = module).exists()