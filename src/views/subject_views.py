from src.serializers.subject_serializers import CreateSubjectSerializer, UpdateSubjectSerializer, \
    ReadSubjectSerializer
from src.services.subject_service import SubjectService
from src.services.school_service import SchoolService
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class SubjectsApiView(ListCreateAPIView):
    """Create school view"""
    serializer_class = CreateSubjectSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        school = SchoolService.get_school_by_id(id=data.get('school'))
        subject = SubjectService.create_subject(
            subject_title=data.get('subject_title'), course=data.get('course'),
            color=data.get('color'), school=school,
            abbreviation=data.get('abbreviation')
        )
        self.serializer_class = ReadSubjectSerializer
        serialized_data = self.serializer_class(subject)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadSubjectSerializer
        self.queryset = SubjectService.get_all_subjects()
        return self.queryset


class SubjectApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy subject api view"""
    serializer_class = UpdateSubjectSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadSubjectSerializer
        self.queryset = SubjectService.get_all_subjects()
        return self.queryset.filter()
