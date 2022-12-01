from src.serializers.school_serializers import CreateSchoolSerializer, UpdateSchoolSerializer, \
    ReadSchoolSerializer
from src.services.school_service import SchoolService
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers


class SchoolsView(ListCreateAPIView):
    """Create and list schools api view"""
    serializer_class = CreateSchoolSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        logo = request.FILES.get('logo')
        school = SchoolService.create_school(name=data.get('name'), location=data.get('location'),
                                             address=data.get('address'), telephone=data.get('telephone'),
                                             motto=data.get('motto'), status=data.get('status'), logo=logo)
        self.serializer_class = ReadSchoolSerializer
        serialized_data = self.serializer_class(school)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadSchoolSerializer
        self.queryset = SchoolService.get_all_schools()
        return self.queryset


class SchoolApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy api view"""
    serializer_class = UpdateSchoolSerializer
    queryset = SchoolService.get_all_schools()

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadSchoolSerializer
        return self.queryset.filter()
