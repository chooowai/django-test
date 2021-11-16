from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def update(self, request, pk):
        request.POST._mutable = True
        request.data['id'] = pk
        request.POST._mutable = False
        return super().update(request)

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def update(self, request, pk):
        request.POST._mutable = True
        request.data['identification_string'] = pk
        request.POST._mutable = False
        return super().update(request)

class SchoolStudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])

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