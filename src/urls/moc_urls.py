from src.views.moc_views import CalenderView, \
    AddFeedback, ListFeedbacks, GetFeedback, \
    CreateCalenderView

from django.urls import path


urlpatterns = [
    path('create-calender', CreateCalenderView.as_view(), name='create-calender'),
    path('calender', CalenderView.as_view(), name='moc-calender'),
    path('send-feedback', AddFeedback.as_view(), name='send-feedback'),
    path('feedback/<id>', GetFeedback.as_view(), name='feednack'),
    path('feedbacks', ListFeedbacks.as_view(), name='feedbacks')
]
