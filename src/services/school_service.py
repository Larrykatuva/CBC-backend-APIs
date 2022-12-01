from src.models.school_models import School
from django.db.models.query import QuerySet


class SchoolService:
    """
    Service to handle all school operations
    """

    @staticmethod
    def create_school(
            name: str,
            location: str,
            address: str,
            telephone: str,
            motto: str,
            status: int,
            logo
    ) -> School:
        """Create new school"""
        return School.objects.create(
            name=name,
            location=location,
            address=address,
            telephone=telephone,
            motto=motto,
            status=status,
            logo=logo
        )

    @staticmethod
    def get_school_by_name(name: str) -> School:
        """Get school by school name"""
        schools = School.objects.filter(name__iexact=name)
        if schools.__len__() > 0:
            return schools[0]
        return None

    @staticmethod
    def get_all_schools() -> QuerySet[School]:
        """Get a list of all schools"""
        return School.objects.all()

    @staticmethod
    def get_school_by_id(id: str) -> School:
        """Get school by id"""
        try:
            return School.objects.get(pk=id)
        except School.DoesNotExist:
            return None

    @staticmethod
    def update_school(
            filter_keys: dict,
            update_values: dict
    ) -> tuple:
        """Update school data"""
        is_updated, updated_row = School.objects.filter(filter_keys).\
            update(update_values)
        return is_updated, updated_row

    @staticmethod
    def filter_schools(filter_keys: dict) -> QuerySet[School]:
        """Filter schools by key"""
        return School.objects.filter(filter_keys)
