from django.contrib import admin
from .models import Module, Registration, Course, CourseModule, courseStudent

admin.site.register(Module)
admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(CourseModule)
admin.site.register(courseStudent)
# Register your models here.
