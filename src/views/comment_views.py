from src.services.comment_service import CommentService
from src.services.feed_service import FeedService
from src.serializers.comment_serilaizers import CreatCommentSerializer, ReadCommentSerializer, \
    UpdateCommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from src.services.notification_service import NotificationService
from threading import Thread


class CommentsApiView(ListCreateAPIView):
    """Create comment view"""
    serializer_class = CreatCommentSerializer
    notification_service = NotificationService()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        feed = FeedService.get_feed_by_id(id=data.get('feed'))
        comment = CommentService.create_comment(
            feed=feed, comment_user=request.user,
            reactions=data.get('reactions'), text=data.get('text')
        )
        thread = Thread(
            target=self.notification_service.notify_comment,
            args=(comment, self.request.user)
        )
        thread.start()
        self.serializer_class = ReadCommentSerializer
        serialized_data = self.serializer_class(comment)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadCommentSerializer
        self.queryset = CommentService.filter_comments(
            {"comment_user": self.request.user}
        )
        return self.queryset


class CommentApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy comment api view"""
    serializer_class = UpdateCommentSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        self.queryset = CommentService.filter_comments(
            {'comment_user': self.request.user}
        )
        if self.request.method == 'GET':
            self.serializer_class = ReadCommentSerializer
        return self.queryset.filter()


class FeedCommentsApiView(ListAPIView):
    serializer_class = ReadCommentSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'feed'

    def get_queryset(self):
        self.queryset = CommentService.filter_comments({
            "feed": self.kwargs.get('feed')
        })
        return self.queryset.filter()

