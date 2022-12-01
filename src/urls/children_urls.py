from django.urls import path
from src.views.child_views import ChildrenApiView, ChildApiView, \
    ChildrenInstanceApiView, ChildInstanceApiView, ChildSubjectApiView, SubjectsAggregateApiView, \
    ListReportsApiView, ReportsApiView


urlpatterns = [
    path('children', ChildrenApiView.as_view(), name='children'),
    path('child/<id>', ChildApiView.as_view(), name='child'),
    path('children-instances', ChildrenInstanceApiView.as_view(), name='child-instances'),
    path('child-instance/<id>', ChildInstanceApiView.as_view(), name='child-instance'),
    path('child-instance/<id>/subjects', ChildSubjectApiView.as_view(), name='child_instance_subjects'),
    path('child-instance/<child_instance>/learning-area', SubjectsAggregateApiView.as_view(),
         name='subject-learning-areas'),
    path('child-instance/create/report', ReportsApiView.as_view(), name='create-report'),
    path('child-instance/<id>/list/reports', ListReportsApiView.as_view(),
         name='list-reports')
]
