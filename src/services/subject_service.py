from django.db.models.query import QuerySet
from src.models.school_models import Subject, School


class SubjectService:
    """
    Class to handle all subject operations
    """

    @staticmethod
    def create_subject(
            subject_title: str,
            course: str,
            color: str,
            school: School,
            abbreviation: str
    ):
        """Create a new subject"""
        return Subject.objects.create(
            subject_title=subject_title,
            course=course,
            color=color,
            school=school,
            abbreviation=abbreviation
        )

    @staticmethod
    def get_subject_id(id: str) -> Subject:
        """Get subject by id"""
        try:
            return Subject.objects.get(pk=id)
        except Subject.DoesNotExist:
            return None

    @staticmethod
    def update_subject(filter_keys: dict, update_data: dict) -> tuple:
        """Update subject values"""
        is_updated, updated_data = Subject.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def filter_subjects(filter_keys: dict) -> QuerySet[Subject]:
        """Filter subjects by keys"""
        return Subject.objects.filter(**filter_keys)

    @staticmethod
    def get_all_subjects() -> QuerySet[Subject]:
        """Get all subjects"""
        return Subject.objects.all()

    @staticmethod
    def get_empty_queryset():
        """Generate empty queryset"""
        return Subject.objects.none()
