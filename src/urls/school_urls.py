from src.views.school_views import SchoolsView, SchoolApiView
from django.urls import path

urlpatterns = [
    path('schools', SchoolsView.as_view(),name='schools'),
    path('school/<id>', SchoolApiView.as_view(), name='school')
]
