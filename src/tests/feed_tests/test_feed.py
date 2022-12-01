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

