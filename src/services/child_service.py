from django.db.models.query import QuerySet
from src.models.school_models import Child
from src.models.user_models import User


class ChildService:
    """
    Class to handle all child operations
    """

    @staticmethod
    def create_child(
            parent: User,
            fullname: str,
            dob: str
    ) -> Child:
        """Create child data"""
        return Child.objects.create(
            parent=parent,
            fullname=fullname,
            dob=dob
        )

    @staticmethod
    def get_all_children() -> QuerySet[Child]:
        """Get all children"""
        return Child.objects.all()

    @staticmethod
    def get_child_by_id(id: str) -> Child:
        """Get child by id"""
        try:
            return Child.objects.get(pk=id)
        except Child.DoesNotExist:
            return None

    @staticmethod
    def update_child(filter_keys: dict, update_data: dict) -> tuple:
        """Update child data"""
        is_updated, updated_data = Child.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def filter_children(filter_keys: dict) -> QuerySet[Child]:
        """Filter children by keys"""
        return Child.objects.filter(**filter_keys)


    