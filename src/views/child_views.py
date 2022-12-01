from src.serializers.child_serializers import CreateChildSerializer, UpdateChildSerializer, \
    ReadChildSerializer
from src.serializers.child_instance_serializers import CreateChildInstanceSerializer, \
    UpdateChildInstanceSerializer, ReadChildInstanceSerializer, SubjectSerializer, LearningAreaSerializer
from src.serializers.reports_serializer import CreateReportSerializer, ReadReportSerializer
from src.services.child_service import ChildService
from src.services.grade_service import GradeService
from src.services.child_instance_service import ChildInstanceService
from src.services.generated_files_service import GenerateFileService
from src.services.subject_service import SubjectService
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ListReportsApiView(ListAPIView):
    """Listing all reports"""
    serializer_class = ReadReportSerializer
    report_service = GenerateFileService()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        child_instance = self.kwargs.get('id')
        print(child_instance)
        self.queryset = self.report_service.filter_reports({
            "child_instance": child_instance
        })
        return self.queryset


class ReportsApiView(CreateAPIView):
    """Create reports view"""
    serializer_class = CreateReportSerializer
    report_service = GenerateFileService()

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        child_instance = ChildInstanceService.get_child_instance_by_id(
            id=data.get('child_instance')
        )
        report = self.report_service.create_report_file(
            filename=data.get('filename'), url=data.get('url'),
            child_instance=child_instance
        )
        self.serializer_class = ReadReportSerializer
        serialized_data = self.serializer_class(report)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )


class ChildSubjectApiView(ListAPIView):
    """Get child subjects view"""
    serializer_class = SubjectSerializer
    child_instance_service = ChildInstanceService()
    subject_service = SubjectService()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        child_instance = self.kwargs.get('id')
        instance = self.child_instance_service.get_child_instance_by_id(
            id=child_instance
        )
        if instance:
            self.queryset = self.subject_service.filter_subjects(
                {"school": instance.grade.school.id}
            )
            return self.queryset
        return self.subject_service.get_empty_queryset()


class SubjectsAggregateApiView(RetrieveAPIView):
    """Learning areas aggregate view"""
    child_instance_service = ChildInstanceService()
    permission_classes = [IsAuthenticated]
    serializer_class = LearningAreaSerializer

    def get(self, request, child_instance):
        data = self.child_instance_service.aggregate_learning_areas(
            child_instance=child_instance
        )
        serialized_data = self.serializer_class(data, many=True)
        return Response(
            data=serialized_data.data, status=status.HTTP_200_OK
        )


class ChildrenApiView(ListCreateAPIView):
    """Create child view"""
    serializer_class = CreateChildSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        child = ChildService.create_child(
            parent=request.user, fullname=data.get('fullname'),
            dob=data.get('dob')
        )
        self.serializer_class = ReadChildSerializer
        serialized_data = self.serializer_class(child)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadChildSerializer
        self.queryset = ChildService.filter_children(
            {"parent": self.request.user}
        )
        return self.queryset


class ChildApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy child api view"""
    serializer_class = UpdateChildSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadChildSerializer
        self.queryset = ChildService.filter_children(
            {"parent": self.request.user}
        )
        return self.queryset.filter()


class ChildrenInstanceApiView(ListCreateAPIView):
    """Create child instance view"""
    serializer_class = CreateChildInstanceSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        grade = GradeService.get_grade_by_id(id=data.get('grade'))
        child = ChildService.get_child_by_id(id=data.get('child'))
        child_instance = ChildInstanceService.create_child_instance(
            child=child, grade=grade
        )
        self.serializer_class = ReadChildInstanceSerializer
        serialized_data = self.serializer_class(child_instance)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        self.serializer_class = ReadChildInstanceSerializer
        children = ChildService.filter_children(
            {"parent": self.request.user}
        )
        children_list = []
        for child in children:
            children_list.append(child.id)
        self.queryset = ChildInstanceService.filter_child_instances(
            {"child__in": children_list}
        )
        return self.queryset


class ChildInstanceApiView(RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy child instance api view"""
    serializer_class = UpdateChildInstanceSerializer

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ReadChildInstanceSerializer
        children = ChildService.filter_children(
            {"parent": self.request.user}
        )
        children_list = []
        for child in children:
            children_list.append(child.id)
        self.queryset = ChildInstanceService.filter_child_instances(
            {"child__in": children_list}
        )
        return self.queryset.filter()
