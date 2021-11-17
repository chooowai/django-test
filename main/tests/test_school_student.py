from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from main.models import Student, School

api_client = APIClient()
school_stub_1 = {
    "name": "School Test 1",
    "max_student": 20,
}
school_stub_2 = {
    "name": "School Test 2",
    "max_student": 10,
}
student_stub_1 = {
    "first_name": "First",
    "last_name": "Student1",
    "gpa": 3.0,
}
student_stub_2 = {
    "first_name": "Second",
    "last_name": "Student2",
    "gpa": 2.5
}
student_stub_3 = {
    "first_name": "Third",
    "last_name": "Student3",
    "gpa": 2.0
}
student_stub_4 = {
    "first_name": "Forth",
    "last_name": "Student4",
    "gpa": 3.0
}

is_set_up = False
class SchoolStudentTest(APITestCase):
    def setUp(self):
        if not is_set_up:
            existing_school_1 = School.objects.create(
                name=school_stub_1['name'], max_student=school_stub_1['max_student'])
            existing_school_2 = School.objects.create(
                name=school_stub_2['name'], max_student=school_stub_2['max_student'])
            Student.objects.create(
                first_name=student_stub_1['first_name'], last_name=student_stub_1['last_name'],
                gpa=student_stub_1['gpa'], school=existing_school_1
            )
            Student.objects.create(
                first_name=student_stub_2['first_name'], last_name=student_stub_2['last_name'],
                gpa=student_stub_2['gpa'], school=existing_school_2
            )
            Student.objects.create(
                first_name=student_stub_3['first_name'], last_name=student_stub_3['last_name'],
                gpa=student_stub_3['gpa'], school=existing_school_1
            )

    def test_get_school_students(self):
        existing_school_id_1 = list(School.objects.all())[0].id
        response = api_client.get(f'/schools/{existing_school_id_1}/students/')
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['count'] == 2
        for student in data['results']:
            assert student['first_name'] == student_stub_1['first_name'] or student['first_name'] == student_stub_3['first_name']
            assert student['last_name'] == student_stub_1['last_name'] or student['last_name'] == student_stub_3['last_name']
            assert float(student['gpa']) == float(student_stub_1['gpa']) or float(student['gpa']) == float(student_stub_3['gpa'])
            assert student['school'] == existing_school_id_1

    def test_get_school_students_filter(self):
        existing_school_id_1 = list(School.objects.all())[0].id
        response = api_client.get(f'/schools/{existing_school_id_1}/students/?gpa=2')
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['count'] == 1
        student = data['results'][0]
        assert student['first_name'] == student_stub_3['first_name']
        pass

    def test_get_school_students_order(self):
        existing_school_id_1 = list(School.objects.all())[0].id
        response = api_client.get(f'/schools/{existing_school_id_1}/students/?ordering=gpa')
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['count'] == 2
        student_1 = data['results'][0]
        assert student_1['first_name'] == student_stub_3['first_name']
        student_2 = data['results'][1]
        assert student_2['first_name'] == student_stub_1['first_name']
        pass

    def test_get_school_students_by_id(self):
        existing_school_id_1 = list(School.objects.all())[0].id
        existing_student = list(Student.objects.filter(school=existing_school_id_1))[0]
        existing_id = existing_student.identification_string
        response = api_client.get(f'/schools/{existing_school_id_1}/students/{existing_id}/')
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert data['first_name'] == existing_student.first_name
        pass

    def test_post_student(self):
        existing_school_id = list(School.objects.all())[0].id
        response = api_client.post(f'/schools/{existing_school_id}/students/', student_stub_4)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert data['school'] == existing_school_id
        assert data['first_name'] == student_stub_4['first_name']
        assert data['last_name'] == student_stub_4['last_name']
        assert float(data['gpa']) == float(student_stub_4['gpa'])

    def test_delete_by_id(self):
        existing_school_id = list(School.objects.all())[0].id
        existing_student = list(Student.objects.filter(school=existing_school_id))[0]
        existing_id = existing_student.identification_string
        response = api_client.delete(f'/schools/{existing_school_id}/students/{existing_id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        response = api_client.get(f'/schools/{existing_school_id}/students/{existing_id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND