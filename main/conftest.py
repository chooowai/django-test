import pytest
from main.models import School
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username="rafal", email="test@example.com")
    return user
@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def test_school_1():
    school, _ = School.objects.get_or_create(
        name="Mahidol",
        max_student=100,
    )
    return school