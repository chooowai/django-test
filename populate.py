# Don't change the format. Order matters!

import os
from random import randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')

import django
django.setup()
from faker import Faker

from main.models import School, Student

faker = Faker()

def populateSchools(N = 10):
    for _ in range(N):
        name = faker.name()
        max_student = randint(10, 50)
        school = School.objects.create(name=name, max_student=max_student)
        populateStudents(school)

def populateStudents(school):
    for _ in range(int(school.max_student/2)):
        name = faker.name()
        first_name = name.split()[0]
        last_name = name.split()[1]
        gpa = randint(1, 4)
        Student.objects.create(first_name=first_name, last_name=last_name, gpa=gpa, school=school)

if __name__ == '__main__':
    print('Populating data...')
    populateSchools(20)
    print('Populating complete')