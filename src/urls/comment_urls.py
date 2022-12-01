from src.views.comment_views import CommentsApiView, CommentApiView, FeedCommentsApiView
from django.urls import path


urlpatterns = [
    path('comments', CommentsApiView.as_view(), name='comments'),
    path('comment/<id>', CommentApiView.as_view(), name="comment"),
    path('comments/<feed>', FeedCommentsApiView.as_view(), name='feed-comments')
]
