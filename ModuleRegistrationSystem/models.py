from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    name = models.CharField(max_length= 20)
    code = models.CharField(max_length= 4)
    credit = models.IntegerField(choices= [(20, 20), (40, 40), (60, 60)])
    category = models.CharField(max_length= 20, choices= [('In-person', 'In person'), ('Online', 'Online')])
    description = models.TextField()
    availability = models.BooleanField(default=True)
    #coursesallowedtoattend = 

    def __str__(self):
        return f'{self.name}'

# Create your models here.
