from django.core.checks.messages import Error
from django.core.exceptions import ValidationError
from rest_framework.fields import Field
from .models import School, Student
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'max_student']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['identification_string', 'first_name', 'last_name', 'gpa', 'school']

    def validate_gpa(self, gpa):
        if gpa < 0 or gpa > 4:
            raise ValidationError(
                "GPA must be between 0 and 4"
            )
        return gpa

    def _validate_school(self, school, identification_string):
        existing_students = list(school.students.all())
        filtered_existing_students = list(filter(lambda stu: stu.identification_string != identification_string, existing_students))
        if len(filtered_existing_students) >= school.max_student:
            raise ValidationError({'school': [f'School {school.name} already has maximum number of students {school.max_student}'],})
        return school

    def validate(self, value):
        school = value.get('school')
        identification_string = value.get('identification_string')
        try:
            self._validate_school(school, identification_string)
        except ValidationError as e:
            raise e
        return value