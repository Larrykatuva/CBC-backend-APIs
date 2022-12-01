from src.views.teacher_views import TeachersApiView, TeacherApiView
from django.urls import path

urlpatterns = [
    path('teachers', TeachersApiView.as_view(), name='teachers'),
    path('teacher/<id>', TeacherApiView.as_view(), name='teacher')
]
