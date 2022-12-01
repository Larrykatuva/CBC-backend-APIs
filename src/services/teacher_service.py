from src.models.school_models import Teacher, School
from django.db.models.query import QuerySet


class TeacherService:
    """
    Class to handle all teacher operations
    """

    @staticmethod
    def create_teacher(
            fullname: str,
            phone: str,
            email: str,
            school: School,
            id_number: str,
            tsc_number: str,
            surname: str,
            other_names: str
    ) -> Teacher:
        """Create teacher"""
        return Teacher.objects.create(
            fullname=fullname,
            phone=phone,
            email=email,
            school=school,
            id_number=id_number,
            tsc_number=tsc_number,
            surname=surname,
            other_names=other_names
        )

    @staticmethod
    def get_all_teachers() -> QuerySet[Teacher]:
        """Get all teachers"""
        return Teacher.objects.all()

    @staticmethod
    def get_teacher_by_id(id: str) -> Teacher:
        """Get teacher by id"""
        try:
            return Teacher.objects.get(pk=id)
        except Teacher.DoesNotExist:
            return None

    @staticmethod
    def update_teacher(
            filter_keys: dict,
            update_values: dict
    ) -> tuple:
        """Update school data"""
        is_updated, updated_row = Teacher.objects.filter(filter_keys). \
            update(update_values)
        return is_updated, updated_row

    @staticmethod
    def get_school_teachers(school: School):
        """Get school teachers"""
        return Teacher.objects.filter(school=school)

    @staticmethod
    def filter_teachers(filter_keys: dict) -> QuerySet[Teacher]:
        """Filter teachers by keys"""
        return Teacher.objects.filter(**filter_keys)


