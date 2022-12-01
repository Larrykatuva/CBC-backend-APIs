from django.urls import path
from src.views.notification_views import ListNotifications

urlpatterns = [
    path('notifications', ListNotifications.as_view(), name='list=notifications')
]
