from django import template
from ModuleRegistrationSystem.models import Registration

register = template.Library()

@register.filter(name = 'if_registered')
def if_registered(student, module):
    return Registration.objects.filter(student = student, module = module).exists()