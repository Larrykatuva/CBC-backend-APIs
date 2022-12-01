from src.services.notification_service import NotificationService
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from src.serializers.notification_serializer import NotificationSerializer


class ListNotifications(ListAPIView):
    serializer_class = NotificationSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.queryset = NotificationService.filter_notifications(
            {"parent": self.request.user}
        )
        return self.queryset
    