from src.serializers.teacher_serializers import CreateTeacherSerializer, ReadTeacherSerializer, \
    UpdateTeacherSerializer
from src.services.teacher_service import TeacherService
from src.services.school_service import SchoolService
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class TeachersApiView(ListCreateAPIView):
    """Create teacher view"""
    serializer_class = CreateTeacherSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        school = SchoolService.get_school_by_id(id=data.get('school'))
        teacher = TeacherService.create_teacher(
            fullname=data.get('fullname'), phone=data.get('phone'), email=data.get('email'),
            school=school, id_number=data.get('id_number'), tsc_number=data.get('tsc_number'),
            surname=data.get('surname'), other_names=data.get('other_names')
        )
        self.serializer_class = ReadTeacherSerializer
        serialized_data = self.serializer_class(teacher)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadTeacherSerializer
        self.queryset = TeacherService.get_all_teachers()
        return self.queryset


class TeacherApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy teacher api view"""
    serializer_class = UpdateTeacherSerializer
    queryset = TeacherService.get_all_teachers()

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadTeacherSerializer
        return self.queryset.filter()
