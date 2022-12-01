from src.views.feed_views import FeedsApiView, FeedApiView, ChildFeedsApiView
from django.urls import path

urlpatterns = [
    path('feeds', FeedsApiView.as_view(), name='feeds'),
    path('feed/<id>', FeedApiView.as_view(), name='feed'),
    path('child/<child_instance>/feeds', ChildFeedsApiView.as_view(), name="child-feeds"),
]
