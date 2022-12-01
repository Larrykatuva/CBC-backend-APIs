from src.views.subject_views import SubjectApiView, SubjectsApiView
from django.urls import path

urlpatterns = [
    path('subjects', SubjectsApiView.as_view(), name='subjects'),
    path('subject/<id>', SubjectApiView.as_view(), name='subject')
]
