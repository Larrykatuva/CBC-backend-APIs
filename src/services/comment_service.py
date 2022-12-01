from src.models.school_models import Feed, Comment
from src.models.user_models import User
from django.db.models.query import QuerySet


class CommentService:
    """
    Class to handle all comment operations
    """

    @staticmethod
    def create_comment(
            feed: Feed,
            comment_user: User,
            reactions: str,
            text: str
    ) -> Comment:
        """Create new comment"""
        return Comment.objects.create(
            feed=feed,
            comment_user=comment_user,
            reactions=reactions,
            text=text
        )

    @staticmethod
    def get_comment_by_id(id: str) -> Comment:
        """Get comment by id"""
        try:
            return Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            return None

    @staticmethod
    def update_comment(filter_keys: dict, update_data: dict) -> tuple:
        """Update comment data"""
        is_updated, updated_data = Comment.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def get_all_comments() -> QuerySet[Comment]:
        """Get all comments"""
        return Comment.objects.all()

    @staticmethod
    def filter_comments(filter_keys: dict) -> QuerySet[Comment]:
        """Filter comments"""
        return Comment.objects.filter(**filter_keys)
