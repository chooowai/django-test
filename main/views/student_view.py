from rest_framework.viewsets import ModelViewSet
from main.utils.pagination import StandardResultsSetPagination
from main.models import Student
from main.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('identification_string')
    # set up filter, sorting and pagination
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ['first_name', 'last_name', 'gpa', 'school']
    ordering_fields = ('first_name', 'last_name', 'gpa', 'school')

    def update(self, request, pk):
        # make sure id from request url param is used for update
        # in case user provides another id in the request
        request.POST._mutable = True
        request.data['identification_string'] = pk
        request.POST._mutable = False
        return super().update(request)