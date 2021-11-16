from rest_framework.viewsets import ModelViewSet

from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SchoolStudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    def get_queryset(self):
        print(self)
        return Student.objects.filter(school=self.kwargs['school_pk'])