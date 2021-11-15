from .models import School, Student
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'max_student']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['identification_string', 'first_name', 'last_name', 'school']

