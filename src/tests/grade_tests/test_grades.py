from src.tests.teacher_tests.moc_data import TeacherMocs
from src.tests.school_tests.moc_data import SchoolMocs
from src.tests.grade_tests.moc_data import GradeMocs
from src.tests.grade_tests.setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestGradeViews(TestSetup):
    """Testing Grade view"""

    def test_cannot_create_unauthenticated(self):
        res = self.client.post(
            path=self.grade_url
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_grade_without_data(self):
        res = self.client.post(
            path=self.grade_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 400)

    def test_can_create_grade(self):
        school = self.client.post(
            path=self.school_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = TeacherMocs().create_data
        data['school'] = school.data.get('id')
        teacher = self.client.post(
            path=self.teachers_url,
            data=data,
            **self.auth_headers
        )
        data = GradeMocs().create_data
        data['school'] = school.data.get('id')
        data['teacher'] = teacher.data.get('id')
        res = self.client.post(
            path=self.grade_url,
            data=data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 201)

    def test_cannot_get_grades_unauthorized(self):
        res = self.client.get(
            path=self.grade_url
        )
        self.assertEqual(res.status_code, 401)

    def test_can_get_grades(self):
        res = self.client.get(
            path=self.grade_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_cannot_get_grade_unauthorized(self):
        school = self.client.post(
            path=self.school_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = TeacherMocs().create_data
        data['school'] = school.data.get('id')
        teacher = self.client.post(
            path=self.teachers_url,
            data=data,
            **self.auth_headers
        )
        data = GradeMocs().create_data
        data['school'] = school.data.get('id')
        data['teacher'] = teacher.data.get('id')
        grade = self.client.post(
            path=self.grade_url,
            data=data,
            **self.auth_headers
        )
        res = self.client.get(
            path=reverse(viewname='grade', args=[grade.data.get('id')])
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_get_grade(self):
        school = self.client.post(
            path=self.school_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = TeacherMocs().create_data
        data['school'] = school.data.get('id')
        teacher = self.client.post(
            path=self.teachers_url,
            data=data,
            **self.auth_headers
        )
        data = GradeMocs().create_data
        data['school'] = school.data.get('id')
        data['teacher'] = teacher.data.get('id')
        grade = self.client.post(
            path=self.grade_url,
            data=data,
            **self.auth_headers
        )
        update_data = GradeMocs().update_data
        update_data['school'] = school.data.get('id')
        update_data['teacher'] = teacher.data.get('id')
        res = self.client.get(
            path=reverse(viewname='grade', args=[grade.data.get('id')]),
            data=update_data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_can_update_grade(self):
        school = self.client.post(
            path=self.school_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = TeacherMocs().create_data
        data['school'] = school.data.get('id')
        teacher = self.client.post(
            path=self.teachers_url,
            data=data,
            **self.auth_headers
        )
        data = GradeMocs().create_data
        data['school'] = school.data.get('id')
        data['teacher'] = teacher.data.get('id')
        grade = self.client.post(
            path=self.grade_url,
            data=data,
            **self.auth_headers
        )
        update_data = GradeMocs().update_data
        update_data['school'] = school.data.get('id')
        update_data['teacher'] = teacher.data.get('id')
        print("\n\n****", update_data, "****\n\n")
        res = self.client.patch(
            path=reverse(viewname='grade', args=[grade.data.get('id')]),
            data=update_data,
            **self.auth_headers
        )
        print("\n\n****", res.data, "****\n\n")
        self.assertEqual(res.status_code, 200)

    def test_can_delete_grade(self):
        school = self.client.post(
            path=self.school_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = TeacherMocs().create_data
        data['school'] = school.data.get('id')
        teacher = self.client.post(
            path=self.teachers_url,
            data=data,
            **self.auth_headers
        )
        data = GradeMocs().create_data
        data['school'] = school.data.get('id')
        data['teacher'] = teacher.data.get('id')
        grade = self.client.post(
            path=self.grade_url,
            data=data,
            **self.auth_headers
        )
        res = self.client.delete(
            path=reverse(viewname='grade', args=[grade.data.get('id')]),
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 204)
