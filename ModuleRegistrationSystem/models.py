from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Module(models.Model):
    name = models.CharField(max_length= 20)
    code = models.CharField(max_length= 4, primary_key= 'code')
    credit = models.IntegerField(choices= [(20, 20), (40, 40), (60, 60)])
    category = models.CharField(max_length= 20, choices= [('In-person', 'In person'), ('Online', 'Online')])
    description = models.TextField()
    availability = models.BooleanField(default=True)
    #coursesallowedtoattend = 

    def __str__(self):
        return f'{self.name}'

class Registration(models.Model):
    student = models.ForeignKey(User,null = True, related_name= 'student_registrations', on_delete = models.CASCADE)
    module = models.ForeignKey(Module, null = True, related_name= 'module_registrations', on_delete = models.CASCADE)
    dateOfRegistration = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.student} registered to {self.module}'


