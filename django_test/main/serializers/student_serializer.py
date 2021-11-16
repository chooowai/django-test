from django.core.exceptions import ValidationError
from main.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['identification_string', 'first_name', 'last_name', 'gpa', 'school']

    # will be automatically called by serializer.validate
    # make sure gpa is between 0 and 4
    def validate_gpa(self, gpa):
        if gpa < 0 or gpa > 4:
            raise ValidationError(
                "GPA must be between 0 and 4"
            )
        return gpa

    # return BadRequest with validation error if school has reached max number of students
    def validate_school_limit(self, school, identification_string):
        # get existing students of school
        existing_students = list(school.students.all())
        # make sure it doesn't count the current student
        filtered_existing_students = list(filter(lambda stu: stu.identification_string != identification_string, existing_students))
        # return ValidationError if max number is reached
        if len(filtered_existing_students) >= school.max_student:
            raise ValidationError({'school': [f'School {school.name} already has maximum number of students {school.max_student}'],})
        return school

    # custom validate method to call validate_school_limit
    # For the purpose of providing multiple fields for validation
    def validate(self, value):
        school = value.get('school')
        identification_string = value.get('identification_string')
        try:
            self.validate_school_limit(school, identification_string)
        except ValidationError as e:
            raise e
        return value