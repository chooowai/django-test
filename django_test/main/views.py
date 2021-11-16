from rest_framework.viewsets import ModelViewSet
from main.pagination import StandardResultsSetPagination
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ['name', 'max_student']
    ordering_fields = ('name', 'max_student')

    def update(self, request, pk):
        request.POST._mutable = True
        request.data['id'] = pk
        request.POST._mutable = False
        return super().update(request)

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ['first_name', 'last_name', 'gpa', 'school']
    ordering_fields = ('first_name', 'last_name', 'gpa', 'school')

    def update(self, request, pk):
        request.POST._mutable = True
        request.data['identification_string'] = pk
        request.POST._mutable = False
        return super().update(request)

class SchoolStudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ['first_name', 'last_name', 'gpa']
    ordering_fields = ('first_name', 'last_name', 'gpa')

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