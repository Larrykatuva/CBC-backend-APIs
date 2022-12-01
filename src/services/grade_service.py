from src.models.school_models import Grade, School, Teacher
from django.db.models.query import QuerySet


class GradeService:
    """
    Grade class to handle all grade operations
    """

    @staticmethod
    def create_grade(
            name: str,
            grade: str,
            school: School,
            class_number: str,
            teacher: Teacher
    ) -> Grade:
        """Create new grade"""
        return Grade.objects.create(
            name=name,
            grade=grade,
            school=school,
            class_number=class_number,
            teacher=teacher
        )

    @staticmethod
    def get_grade_by_id(id: str) -> Grade:
        """Get grade by id"""
        try:
            return Grade.objects.get(pk=id)
        except Grade.DoesNotExist:
            return None

    @staticmethod
    def update_grades(filter_keys: dict, update_data: dict) -> tuple:
        """Update grade data"""
        is_updated, updated_data = Grade.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def get_all_grades() -> QuerySet[Grade]:
        """Get all grades"""
        return Grade.objects.all()

    @staticmethod
    def filter_grades(filter_keys) -> QuerySet[Grade]:
        """Filter grades"""
        return Grade.objects.filter(**filter_keys)