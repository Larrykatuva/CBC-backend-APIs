from django.urls import path
from src.views.grade_views import GradesApiView, GradeApiView


urlpatterns = [
    path('grades', GradesApiView.as_view(), name='grades'),
    path('grade/<id>', GradeApiView.as_view(), name='grade')
]
