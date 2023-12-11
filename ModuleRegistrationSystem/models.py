from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Course(models.Model):
    name = models.CharField(max_length = 20, primary_key= 'name')
    startDate = models.DateField(default = timezone.now)
    duration = models.CharField(max_length = 10 ,choices= [('1 year', '1 year'), ('2 years', '2 years'), ('3 years', '3 years')])
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Module(models.Model):
    name = models.CharField(max_length= 40)
    code = models.CharField(max_length= 4, primary_key= 'code')
    credit = models.IntegerField(choices= [(20, 20), (40, 40), (60, 60)])
    category = models.CharField(max_length= 20, choices= [('In-person', 'In person'), ('Online', 'Online')])
    description = models.TextField()
    availability = models.BooleanField(default=True)
    courses_Allowed_To_Register = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('ModuleRegistrationSystem:module-detail', kwargs = {'pk': self.pk})
    
class Registration(models.Model):
    student = models.ForeignKey(User,null = True, related_name= 'studentregistrations', on_delete = models.CASCADE)
    module = models.ForeignKey(Module, null = True, related_name= 'moduleregistrations', on_delete = models.CASCADE)
    dateOfRegistration = models.DateTimeField(default = timezone.now)

    class Meta:
        unique_together = ('student', 'module')
        
    def __str__(self):
        return f'{self.student} is registered to {self.module}'
    
    def get_absolute_url(self):
        return reverse('ModuleRegistrationSystem:home')
    


