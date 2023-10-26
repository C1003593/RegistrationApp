from django.urls import path
from . import views

app_name = 'ModuleRegistrationSystem'

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about', views.about_us, name='about us'),
    path('contact', views.contact_us, name='contact us'),
    path('modules', views.modules, name='modules'),
]