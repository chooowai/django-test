from rest_framework.viewsets import ModelViewSet
from main.utils.pagination import StandardResultsSetPagination
from main.models import School
from main.serializers import SchoolSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all().order_by('id')
    serializer_class = SchoolSerializer
    # set up filter, sorting and pagination
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ['name', 'max_student']
    ordering_fields = ('name', 'max_student')

    def update(self, request, pk):
        # make sure id from request url param is used for update
        # in case user provides another id in the request
        request.POST._mutable = True
        request.data['id'] = pk
        request.POST._mutable = False
        return super().update(request)