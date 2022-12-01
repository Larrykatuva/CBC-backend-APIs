from src.tests.teacher_tests.moc_data import TeacherMocs
from src.tests.school_tests.moc_data import SchoolMocs
from src.tests.teacher_tests.setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestTeachersView(TestSetup):
    """Testing teachers view"""

    def test_cannot_create_teacher_unauthenticated(self):
        res = self.client.post(
            path=self.teachers_url,
            data=TeacherMocs().create_data
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_teacher_without_data(self):
        res = self.client.post(
            path=self.teachers_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 400)

    def test_can_create_teacher(self):
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
        self.assertEqual(teacher.status_code, 201)

    def test_cannot_get_teachers_unauthorized(self):
        res = self.client.get(
            path=self.teachers_url
        )
        self.assertEqual(res.status_code, 401)

    def test_can_get_teachers(self):
        res = self.client.get(
            path=self.teachers_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_cannot_update_teacher_unauthorized(self):
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
        res = self.client.patch(
            path=reverse(viewname='teacher', args=[teacher.data.get('id')])
        )
        self.assertEqual(res.status_code, 401)

    def test_can_update_teacher(self):
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
        update_data = TeacherMocs().update_data
        update_data['school'] = school.data.get('id')
        res = self.client.patch(
            path=reverse(viewname='teacher', args=[teacher.data.get('id')]),
            data=update_data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_can_get_teacher_by_id(self):
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
        res = self.client.get(
            path=reverse(viewname='teacher', args=[teacher.data.get('id')]),
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_can_delete_teacher_by_id(self):
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
        res = self.client.delete(
            path=reverse(viewname='teacher', args=[teacher.data.get('id')]),
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 204)

