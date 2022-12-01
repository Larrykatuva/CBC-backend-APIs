from src.tests.school_tests.setup import TestSetup
from src.tests.school_tests.moc_data import SchoolMocs
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestSchoolViews(TestSetup):
    """Testing school view"""

    def test_cannot_create_school_unauthenticated(self):
        res = self.client.post(path=self.schools_url,
                               data=SchoolMocs().create_data)
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_school_without_data(self):
        res = self.client.post(
            path=self.schools_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 400)

    def test_can_create_school(self):
        res = self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 201)

    def test_cannot_get_schools_unauthenticated(self):
        res = self.client.get(path=self.schools_url)
        self.assertEqual(res.status_code, 401)

    def test_can_get_schools(self):
        res = self.client.get(
            path=self.schools_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_cannot_get_school_by_wrong_id(self):
        self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        self.client.get(
            path=self.schools_url,
            **self.auth_headers
        )
        school = self.client.get(
            path=reverse(viewname='school',
                         args=['wrong']),
            **self.auth_headers
        )
        self.assertEqual(school.status_code, 404)

    def test_can_get_school(self):
        self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        schools = self.client.get(
            path=self.schools_url,
            **self.auth_headers
        )
        school = self.client.get(
            path=reverse(viewname='school',
                         args=[schools.data.get('results')[0].get('id')]),
            **self.auth_headers
        )
        self.assertEqual(school.status_code, 200)

    def test_cannot_update_school_with_wrong_id(self):
        self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        self.client.get(
            path=self.schools_url,
            **self.auth_headers
        )
        school = self.client.patch(
            path=reverse(viewname='school',
                         args=['wrong']),
            data=SchoolMocs().update_data,
            **self.auth_headers
        )
        self.assertEqual(school.status_code, 404)

    def test_can_update_school(self):
        self.client.post(
            path=self.schools_url,
            data=SchoolMocs().create_data,
            **self.auth_headers
        )
        schools = self.client.get(
            path=self.schools_url,
            **self.auth_headers
        )
        school = self.client.patch(
            path=reverse(viewname='school',
                         args=[schools.data.get('results')[0].get('id')]),
            data=SchoolMocs().update_data,
            **self.auth_headers
        )
        self.assertEqual(school.status_code, 200)


