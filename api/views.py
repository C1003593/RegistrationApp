from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ModuleRegistrationSystem.models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('startDate')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

# Create your views here.
