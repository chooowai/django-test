from main.models import School
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'max_student']