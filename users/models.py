from django.db import models
from django.contrib.auth.models import User
from ModuleRegistrationSystem.models import Course

class studentAccount(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    DOB = models.DateField(null = True)
    Address = models.CharField(max_length=30, null = True)
    City = models.CharField(max_length=20, null = True)
    Country = models.CharField(max_length=20, null = True)
    image = models.ImageField(default = 'default.png', upload_to= 'profile_pics')
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


