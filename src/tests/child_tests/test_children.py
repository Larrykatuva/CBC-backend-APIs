from src.tests.teacher_tests.moc_data import TeacherMocs
from src.tests.school_tests.moc_data import SchoolMocs
from src.tests.grade_tests.moc_data import GradeMocs
from src.tests.child_tests.moc_data import ChildMocs
from src.tests.child_tests.setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestChildrenViews(TestSetup):
    """Testing children view"""

    def test_cannot_create_unauthenticated(self):
        res = self.client.post(
            path=self.children_url
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_child_without_data(self):
        res = self.client.post(
            path=self.children_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 400)

    def test_can_create_child(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        res = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 201)

    def test_cannot_get_children_unauthenticated(self):
        res = self.client.get(
            path=self.children_url
        )
        self.assertEqual(res.status_code, 401)

    def test_can_get_children(self):
        res = self.client.get(
            path=self.children_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_cannot_get_child_by_id_unauthenticated(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        res = self.client.get(
            path=reverse(viewname='child', args=[child.data.get('id')])
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_get_child_with_wrong_id(self):
        res = self.client.get(
            path=reverse(viewname='child', args=['wrong']),
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 404)

    def test_can_update_child(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        update_data = ChildMocs().update_data
        update_data['grade'] = grade.data.get('id')
        res = self.client.patch(
            path=reverse(viewname='child', args=[child.data.get('id')]),
            data=update_data,
            **self.auth_headers
        )
        self.assertEqual(200, 200)

    def test_can_delete_child(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        res = self.client.delete(
            path=reverse(viewname='child', args=[child.data.get('id')]),
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 204)

    def test_cannot_create_child_instance_unauthenticated(self):
        res = self.client.post(
            path=self.child_instances_url
        )
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_child_instance_without_data(self):
        res = self.client.post(
            path=self.child_instances_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 400)

    def test_can_create_child_instance(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        child_instance = {
            "child": child.data.get('id'),
            "grade": grade.data.get('id')
        }
        res = self.client.post(
            path=self.child_instances_url,
            data=child_instance,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 201)

    def test_cannot_get_child_instances_unauthenticated(self):
        res = self.client.get(
            path=self.child_instances_url
        )
        self.assertEqual(res.status_code, 401)

    def test_can_get_child_instances(self):
        res = self.client.get(
            path=self.child_instances_url,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_cannot_update_child_instance_unauthorized(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        child_instance = {
            "child": child.data.get('id'),
            "grade": grade.data.get('id')
        }
        new_child_instance = self.client.post(
            path=self.child_instances_url,
            data=child_instance,
            **self.auth_headers
        )
        res = self.client.patch(
            path=reverse('child-instance', args=[new_child_instance.data.get('id')]),
            data=child_instance
        )
        self.assertEqual(res.status_code, 401)

    def test_can_update_child_instance(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        child_instance = {
            "child": child.data.get('id'),
            "grade": grade.data.get('id')
        }
        new_child_instance = self.client.post(
            path=self.child_instances_url,
            data=child_instance,
            **self.auth_headers
        )
        res = self.client.patch(
            path=reverse('child-instance', args=[new_child_instance.data.get('id')]),
            data=child_instance,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_can_get_child_by_id(self):
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
        data = ChildMocs().create_data
        data['grade'] = grade.data.get('id')
        child = self.client.post(
            path=self.children_url,
            data=data,
            **self.auth_headers
        )
        child_instance = {
            "child": child.data.get('id'),
            "grade": grade.data.get('id')
        }
        new_child_instance = self.client.post(
            path=self.child_instances_url,
            data=child_instance,
            **self.auth_headers
        )
        res = self.client.get(
            path=reverse('child-instance', args=[new_child_instance.data.get('id')]),
            data=child_instance,
            **self.auth_headers
        )
        self.assertEqual(res.status_code, 200)

