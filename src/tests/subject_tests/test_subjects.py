from src.tests.subject_tests.setup import TestSetup
from src.tests.school_tests.moc_data import SchoolMocs
from src.tests.subject_tests.moc_data import SubjectMocs
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestSubjectsViews(TestSetup):
    """Testing subjects views"""

    def test_cannot_create_subject_unauthorized(self):
        res = self.client.post(
            path=self.subject_url
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_subject_without_data(self):
        res = self.client.post(
            path=self.subject_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 400)

    def test_can_subject(self):
        school = self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = SubjectMocs().create_data
        data['school'] = school.data.get('id')
        res = self.client.post(
            path=self.subject_url,
            data=data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 201)

    def test_cannot_get_subjects_unauthorized(self):
        res = self.client.get(
            path=self.subject_url
        )
        self.assertEqual(res.status_code, 401)

    def test_can_get_subjects(self):
        res = self.client.get(
            path=self.subject_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_cannot_update_subject_unauthorized(self):
        school = self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = SubjectMocs().create_data
        data['school'] = school.data.get('id')
        subject = self.client.post(
            path=self.subject_url,
            data=data,
            **self.auth_headers
        )
        update_data = SubjectMocs().update_data
        update_data['school'] = subject.data.get('id')
        res = self.client.patch(
            path=reverse(viewname='subject', args=[subject.data.get('id')]),
            data=update_data
        )
        self.assertEqual(res.status_code, 401)

    def test_can_update_subject(self):
        school = self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = SubjectMocs().create_data
        data['school'] = school.data.get('id')
        subject = self.client.post(
            path=self.subject_url,
            data=data,
            **self.auth_headers
        )
        update_data = SubjectMocs().update_data
        update_data['school'] = school.data.get('id')
        res = self.client.patch(
            path=reverse(viewname='subject', args=[subject.data.get('id')]),
            data=update_data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_can_get_subject_by_id(self):
        school = self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        data = SubjectMocs().create_data
        data['school'] = school.data.get('id')
        subject = self.client.post(
            path=self.subject_url,
            data=data,
            **self.auth_headers
        )
        res = self.client.get(
            path=reverse(viewname='subject', args=[subject.data.get('id')]),
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)
