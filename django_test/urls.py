from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from main.views import SchoolViewSet, StudentViewSet, SchoolStudentViewSet

# for index page
default_router = DefaultRouter()
default_router.register('schools', SchoolViewSet)
default_router.register('students', StudentViewSet)

schools_router = routers.NestedSimpleRouter(default_router, r'schools', lookup='school')
schools_router.register(r'students', SchoolStudentViewSet, basename='school-students')

urlpatterns = [
    path('', include(default_router.urls)),
    path(r'', include(schools_router.urls)),
]
