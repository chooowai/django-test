from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from main.models import School

api_client = APIClient()
school_stub_1 = {
    "name": "School Test 1",
    "max_student": 20,
}
school_stub_2 = {
    "name": "School Test 2",
    "max_student": 10,
}
school_stub_3 = {
    "name": "School Test 3",
    "max_student": 15,
}
is_set_up = False
class SchoolTest(APITestCase):
    def setUp(self):
        if not is_set_up:
            School.objects.create(
                name=school_stub_1['name'], max_student=school_stub_1['max_student'])
            School.objects.create(
                name=school_stub_2['name'], max_student=school_stub_2['max_student'])

    def test_get_school(self):
        response = api_client.get("/schools/")
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['count'] == 2
        school_1 = data['results'][0]
        assert school_1['name'] == school_stub_1['name']
        assert school_1['max_student'] == school_stub_1['max_student']
        school_2 = data['results'][1]
        assert school_2['name'] == school_stub_2['name']
        assert school_2['max_student'] == school_stub_2['max_student']
        pass

    def test_get_school_filter(self):
        response = api_client.get("/schools/?max_student=10")
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['count'] == 1
        school_1 = data['results'][0]
        assert school_1['name'] == school_stub_2['name']
        assert school_1['max_student'] == school_stub_2['max_student']
        pass

    def test_get_school_order(self):
        response = api_client.get("/schools/?ordering=max_student")
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['count'] == 2
        school_1 = data['results'][0]
        assert school_1['name'] == school_stub_2['name']
        assert school_1['max_student'] == school_stub_2['max_student']
        school_2 = data['results'][1]
        assert school_2['name'] == school_stub_1['name']
        assert school_2['max_student'] == school_stub_1['max_student']
        pass

    def test_get_by_id(self):
        existing_id = list(School.objects.all())[0].id
        response = api_client.get(f'/schools/{existing_id}/')
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['name'] == school_stub_1['name']
        assert data['max_student'] == school_stub_1['max_student']

    def test_post_school(self):
        response = api_client.post('/schools/', school_stub_3)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert data['name'] == school_stub_3['name']
        assert data['max_student'] == school_stub_3['max_student']

    def test_post_school_no_name(self):
        response = api_client.post('/schools/', {"max_student": 5})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.data
        assert 'name' in data.keys()

    def test_put_by_id(self):
        existing_id = list(School.objects.all())[0].id
        response = api_client.put(f'/schools/{existing_id}/', school_stub_3)
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['name'] == school_stub_3['name']
        assert data['max_student'] == school_stub_3['max_student']

    def test_delete_by_id(self):
        existing_id = list(School.objects.all())[0].id
        response = api_client.delete(f'/schools/{existing_id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        response = api_client.get(f'/schools/{existing_id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND