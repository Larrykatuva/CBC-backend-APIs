from src.serializers.feed_serializers import CreateFeedSerializer, UpdateFeedSerializer, \
    ReadFeeSerializer
from src.services.feed_service import FeedService
from src.services.teacher_service import TeacherService
from src.services.child_instance_service import ChildInstanceService
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from threading import Thread
from src.services.notification_service import NotificationService
from rest_framework import status


class FeedsApiView(ListCreateAPIView):
    """Create feed view"""
    serializer_class = CreateFeedSerializer
    notification_service = NotificationService()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        teacher = TeacherService.get_teacher_by_id(id=data.get('teacher'))
        child_instance = ChildInstanceService.get_child_instance_by_id(
            id=data.get('child_instance')
        )
        feed = FeedService.create_feed(
            teacher=teacher, learning_area=data.get('learning_area'), strand=data.get('strand'),
            substrand=data.get('substrand'), indicator=data.get('indicator'),
            assessment_type=data.get('assessment_type'), assessment_description=data.get('assessment_description'),
            assessment_score=data.get('assessment_score'), assessment_comment=data.get('assessment_comment'),
            learning_outcome=data.get('learning_outcome'), child_instance=child_instance
        )
        thread = Thread(
            target=self.notification_service.notify_feeds,
            args=(feed, self.request.user)
        )
        thread.start()
        self.serializer_class = ReadFeeSerializer
        serialized_data = self.serializer_class(feed)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadFeeSerializer
        self.queryset = FeedService.get_all_feeds()
        return self.queryset


class FeedApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy feed api view"""
    serializer_class = UpdateFeedSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadFeeSerializer
        self.queryset = FeedService.get_all_feeds()
        return self.queryset.filter()


class ChildFeedsApiView(ListAPIView):
    serializer_class = ReadFeeSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'child_instance'

    def get_queryset(self):
        self.queryset = FeedService.filter_feeds({
            "child_instance": self.kwargs.get('child_instance')
        })
        return self.queryset.filter()


