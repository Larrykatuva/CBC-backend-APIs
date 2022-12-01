from src.serializers.app_serializers import CreateAppSerializer, UpdateAppSerializer, ManagerSerializer,\
    ReadAppSerializer
from src.services.app_service import AppService
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, serializers


class RegisterAppView(CreateAPIView):
    """View to register new application"""
    serializer_class = CreateAppSerializer
    app_service = AppService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        client_id = self.app_service.generate_client_id()
        client_secret = self.app_service.generate_client_secret()
        app = self.app_service.register_app(
            name=data.get('name'),
            manager=data.get('manager'),
            client_id=client_id,
            client_secret=client_secret
        )
        self.serializer_class = ReadAppSerializer
        serialized_data = self.serializer_class(app)
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class AppView(RetrieveUpdateDestroyAPIView):
    """
    View to handle:
     - Get app by id
     - Update app by id
     - Delete app by id
    """
    serializer_class = UpdateAppSerializer
    app_service = AppService()
    lookup_field = 'id'

    def get_queryset(self):
        self.queryset = self.app_service.get_all_apps()
        self.serializer_class = ReadAppSerializer
        return self.queryset.filter()


class ManagerAppsView(CreateAPIView):
    """View to get all apps by manager"""
    serializer_class = ManagerSerializer
    app_service = AppService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        apps = self.app_service.get_apps_by_manager(
            manager=data.get('manager')
        )
        self.serializer_class = ReadAppSerializer
        serialized_data = self.serializer_class(apps, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class AllAppsView(ListAPIView):
    """Get list of all apps"""
    serializer_class = ReadAppSerializer
    app_service = AppService()

    def get_queryset(self):
        self.queryset = self.app_service.get_all_apps()
        return self.queryset
