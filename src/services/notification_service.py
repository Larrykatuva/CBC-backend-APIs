import requests
from config.settings import SINGLE_URL, AUTH_KEY
from src.models.school_models import Feed, Comment, User
from django.db.models.query import QuerySet
from src.models.school_models import Notification
import json


class NotificationService:

    @staticmethod
    def post_single_notification(data) -> None:
        """Send notification to firebase"""
        headers = {'Content-type': 'application/json', 'Authorization': AUTH_KEY}
        try:
            res = requests.post(
                url=SINGLE_URL,
                data=json.dumps(data),
                headers=headers
            )
            print(res.status_code)
            print(res.json())
        except Exception as err:
            print("Error")
            print(err)
            pass

    def notify_feeds(self, feed: Feed, parent: User) -> None:
        """Trigger and save a feed notification"""
        print(parent.device_id)
        data = {
            "to": parent.device_id,
            "priority": "high",
            "notification": {
                "title": "Dress them warm",
                "body": "Regarding the off-sett of the cold season, you are advised to ensure your kid dresses warm while coming to school to avoid catching cold."
            },
            "data": {
                "feed": {
                    "id": feed.id.__str__(),
                    "posterImageUrl": "https://cdn.pixabay.com/photo/2022/04/13/04/57/woman-7129432_1280.jpg",
                    "posterName": feed.learning_area,
                    "postedTimestamp": 0,
                    "feedType": feed.assessment_type,
                    "isSeen": False,
                    "description": feed.assessment_description,
                    "feedPictureUrl": "https://cdn.pixabay.com/photo/2022/04/13/04/57/woman-7129432_1280.jpg",
                    "feedId": 0,
                    "expectation": "Test expectation",
                    "breadcrumb": "string",
                    "created-at": feed.created_at.__str__(),
                    "indicator": feed.indicator,
                    "teacher": feed.teacher.fullname,
                    "feed_obj": self.prepare_feed_json(
                        feed=feed
                    )
                },
                "comment": None,
                "general": "Go to notifications page!"
            }
        }
        Notification.objects.create(
            feed=feed,
            body=feed.learning_outcome,
            title=feed.learning_area,
            type="feed",
            parent=parent
        )
        self.post_single_notification(
            data=data
        )

    def notify_comment(self, comment: Comment, parent: User) -> None:
        """Trigger and fire a comment notification"""
        data = {
            "to": parent.device_id,
            "priority": "high",
            "notification": {
                "title": "You have a new comment",
                "body": comment.text
            },
            "data": {
                "comment": {
                    "feed": {
                        "id": comment.feed.id.__str__(),
                        "posterImageUrl": "https://cdn.pixabay.com/photo/2022/04/13/04/57/woman-7129432_1280.jpg",
                        "posterName": comment.feed.learning_area,
                        "postedTimestamp": 0,
                        "feedType": comment.feed.assessment_type,
                        "isSeen": False,
                        "description": comment.feed.assessment_description,
                        "feedPictureUrl": "https://cdn.pixabay.com/photo/2022/04/13/04/57/woman-7129432_1280.jpg",
                        "feedId": 0,
                        "expectation": "Test expectation",
                        "breadcrumb": "string",
                        "created-at": comment.feed.created_at.__str__(),
                        "indicator": comment.feed.indicator,
                        "teacher": comment.feed.teacher.fullname,
                        "feed_obj": self.prepare_feed_json(
                            feed=comment.feed
                        )
                    }
                },
                "feed": None,
                "general": "Go to notifications page!"
            }
        }
        Notification.objects.create(
            comment=comment,
            body=comment.text,
            title="You have a new comment",
            type='comment',
            parent=parent
        )
        self.post_single_notification(
            data=data
        )

    @staticmethod
    def filter_notifications(
            filter_keys: dict
    ) -> QuerySet[Notification]:
        """Filter notifications by keys"""
        return Notification.objects.filter(
            **filter_keys
        )

    @staticmethod
    def prepare_feed_json(feed: Feed):
        """Converting feed object to json"""
        return {
            "id": feed.id.__str__(),
            "teacher": feed.teacher.fullname,
            "learning_area": feed.learning_area,
            "strand": feed.strand,
            "substrand": feed.substrand,
            "indicator": feed.indicator,
            "assessment_type": feed.assessment_type,
            "assessment_description": feed.assessment_description,
            "assessment_score": feed.assessment_score,
            "assessment_comment": feed.assessment_comment,
            "learning_outcome": feed.learning_outcome,
            "child_instance": feed.child_instance.__str__(),
            "assessment_at": feed.assessment_at.__str__(),
            "created_at": feed.created_at.__str__()
        }

