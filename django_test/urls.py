from django.urls import path, include
from rest_framework_nested import routers
from main.views import SchoolViewSet, StudentViewSet, SchoolStudentViewSet

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)

schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', SchoolStudentViewSet, basename='school-students')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(schools_router.urls)),
]
