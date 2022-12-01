from src.models.school_models import Feed, Teacher, ChildInstance
from django.db.models.query import QuerySet
from django.db.models import Count


class FeedService:
    """
    Class to handle feed operations
    """

    @staticmethod
    def create_feed(
            teacher: Teacher,
            learning_area: str,
            strand: str,
            substrand: str,
            indicator: str,
            assessment_type: str,
            assessment_description: str,
            assessment_score: str,
            assessment_comment: str,
            learning_outcome: str,
            child_instance: ChildInstance
    ) -> ChildInstance:
        """Create child instance"""
        return Feed.objects.create(
            teacher=teacher,
            learning_area=learning_area,
            strand=strand,
            substrand=substrand,
            indicator=indicator,
            assessment_type=assessment_type,
            assessment_description=assessment_description,
            assessment_score=assessment_score,
            assessment_comment=assessment_comment,
            learning_outcome=learning_outcome,
            child_instance=child_instance
        )

    @staticmethod
    def get_feed_by_id(id: str) -> Feed:
        """Get feed by id"""
        try:
            return Feed.objects.get(pk=id)
        except Feed.DoesNotExist:
            return None

    @staticmethod
    def update_feed(filter_keys: dict, update_data: dict) -> tuple:
        """Updated feed"""
        is_updated, updated_data = Feed.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def get_all_feeds() -> QuerySet[Feed]:
        """Get all feeds"""
        return Feed.objects.all()

    @staticmethod
    def filter_feeds(filter_keys) -> QuerySet[Feed]:
        """Filter feeds"""
        return Feed.objects.filter(**filter_keys).prefetch_related(
            'comment_feeds'
        ).annotate(Count('comment_feeds'))
