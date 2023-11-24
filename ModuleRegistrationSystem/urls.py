from django.urls import path
from . import views
from .views import PostDetailView, PostListView, PostCreateView

app_name = 'ModuleRegistrationSystem'

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('modules', PostListView.as_view(), name='modules'),
    path('module/new', PostCreateView.as_view(), name = 'module-create'),
    path('module/<str:pk>', PostDetailView.as_view(), name='module-detail'),
    
    

]