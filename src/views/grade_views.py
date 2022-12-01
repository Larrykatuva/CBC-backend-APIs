from src.serializers.grade_serializers import CreateGradeSerializer, UpdateGradeSerializer, \
    ReadGradeSerializer
from src.services.grade_service import GradeService
from src.services.school_service import SchoolService
from src.services.teacher_service import TeacherService
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class GradesApiView(ListCreateAPIView):
    """Create grade view"""
    serializer_class = CreateGradeSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        school = SchoolService.get_school_by_id(id=data.get('school'))
        teacher = TeacherService.get_teacher_by_id(id=data.get('teacher'))
        grade = GradeService.create_grade(
            name=data.get('name'), grade=data.get('grade'), school=school,
            class_number=data.get('class_number'), teacher=teacher
        )
        self.serializer_class = ReadGradeSerializer
        serialized_data = self.serializer_class(grade)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadGradeSerializer
        self.queryset = GradeService.get_all_grades()
        return self.queryset


class GradeApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy grade api view"""
    serializer_class = UpdateGradeSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadGradeSerializer
        self.queryset = GradeService.get_all_grades()
        return self.queryset.filter()
