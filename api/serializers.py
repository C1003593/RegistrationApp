from rest_framework.serializers import ModelSerializer
from ModuleRegistrationSystem.models import Course

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'startDate', 'duration', 'description']