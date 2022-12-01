from src.models.school_models import Child, Grade, ChildInstance, Feed
from django.db.models.query import QuerySet
from django.db.models import Avg


class ChildInstanceService:
    """
    Class to handle child instance operations
    """

    @staticmethod
    def create_child_instance(
            child: Child,
            grade: Grade
    ) -> ChildInstance:
        """Create new child instance"""
        return ChildInstance.objects.create(
            child=child,
            grade=grade
        )

    @staticmethod
    def get_child_instance_by_id(id: str) -> ChildInstance:
        """Get child instance by id"""
        try:
            return ChildInstance.objects.get(pk=id)
        except Exception as er:
            return None

    @staticmethod
    def update_child_instance(filter_keys: dict, update_data: dict) -> tuple:
        """Update child instance"""
        is_updated, updated_data = ChildInstance.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def get_all_child_instances() -> QuerySet[ChildInstance]:
        """Get all child instances"""
        return ChildInstance.objects.all()

    @staticmethod
    def filter_child_instances(filter_keys) -> QuerySet[ChildInstance]:
        """Filter child instances"""
        return ChildInstance.objects.filter(**filter_keys)

    def aggregate_learning_areas(self, child_instance: ChildInstance):
        learning_areas = Feed.objects.filter(child_instance=child_instance).values('learning_area').annotate(average=Avg('assessment_score')).order_by()
        data = []
        for learning_area in learning_areas:
            strands = Feed.objects.filter(learning_area=learning_area.get('learning_area')).values('strand').annotate(
                average=Avg('assessment_score'))
            print(strands.query)
            data.append({
                "learning_area": learning_area.get('learning_area'),
                "average": learning_area.get('average'),
                "strand": strands
            })
        print(Feed.objects.filter(child_instance=child_instance).values('learning_area').annotate(average=Avg('assessment_score')).order_by())
        return data
