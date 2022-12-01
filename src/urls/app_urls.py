from django.urls import path
from src.views.app_views import RegisterAppView, AppView, ManagerAppsView, AllAppsView


urlpatterns = [
    path('create-app', RegisterAppView.as_view(), name='create-app'),
    path('app/<id>', AppView.as_view(), name='app'),
    path('manager-apps', ManagerAppsView.as_view(), name='manager-apps'),
    path('all-apps', AllAppsView.as_view(), name='all-apps')
]
