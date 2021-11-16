from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer
class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()
        name = self.request.query_params.get('name')
        max_student = self.request.query_params.get('max_student')
        if name is not None:
            queryset = queryset.filter(name=name)
        if max_student is not None:
            queryset = queryset.filter(max_student=max_student)
        return queryset

    def update(self, request, pk):
        request.POST._mutable = True
        request.data['id'] = pk
        request.POST._mutable = False
        return super().update(request)

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_queryset(self):
        queryset = Student.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        gpa = self.request.query_params.get('gpa')
        school = self.request.query_params.get('school')
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)
        if gpa is not None:
            queryset = queryset.filter(gpa=gpa)
        if school is not None:
            queryset = queryset.filter(school=school)
        return queryset

    def update(self, request, pk):
        request.POST._mutable = True
        request.data['identification_string'] = pk
        request.POST._mutable = False
        return super().update(request)

class SchoolStudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    def get_queryset(self):
        queryset = Student.objects.filter(school=self.kwargs['school_pk'])
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        gpa = self.request.query_params.get('gpa')
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)
        if gpa is not None:
            queryset = queryset.filter(gpa=gpa)
        return queryset

    def create(self, request, school_pk):
        request.POST._mutable = True
        request.data['school'] = school_pk
        request.POST._mutable = False
        return super().create(request)

    def update(self, request, school_pk, pk):
        request.POST._mutable = True
        request.data['identification_string'] = pk
        if 'school' not in request.data:
            request.data['school'] = school_pk
        request.POST._mutable = False
        return super().update(request)