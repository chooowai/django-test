from rest_framework.viewsets import ModelViewSet
from main.utils.pagination import StandardResultsSetPagination
from main.models import Student
from main.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class SchoolStudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    # set up filter, sorting and pagination
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ['first_name', 'last_name', 'gpa']
    ordering_fields = ('first_name', 'last_name', 'gpa')

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk']).order_by('identification_string')

    def create(self, request, school_pk):
        request.POST._mutable = True
        # make sure school_id from request url param is for user creation
        # in case user provides another school_id in the request
        request.data['school'] = school_pk
        request.POST._mutable = False
        return super().create(request)

    def update(self, request, school_pk, pk):
        request.POST._mutable = True
        # make sure student_id from request url param is used for update
        # handles in case user provide another student_id in the request
        request.data['identification_string'] = pk
        # use school_id from url if not provided
        # allows user to change school of a student
        if 'school' not in request.data:
            request.data['school'] = school_pk
        request.POST._mutable = False
        return super().update(request)