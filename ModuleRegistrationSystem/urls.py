from django.urls import path
from . import views
from .views import ModuleDetailView, ModuleListView, ModuleCreateView, ModuleUpdateView, ModuleDeleteView
from .views import CourseDetailView
from .views import RegistrationView

app_name = 'ModuleRegistrationSystem'

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    
    path('modules', ModuleListView.as_view(), name='modules'),
    path('module/new', ModuleCreateView.as_view(), name = 'module-create'),
    path('module/<str:pk>', ModuleDetailView.as_view(), name='module-detail'),
    path('module/<str:pk>/update/', ModuleUpdateView.as_view(), name='module-update'),
    path('module/<str:pk>/delete/', ModuleDeleteView.as_view(), name='module-delete'),
    path('course/<str:pk>', CourseDetailView.as_view(), name = 'course-detail'),
    path('registration/<str:username>', RegistrationView.as_view(), name='registrations'),
    

]