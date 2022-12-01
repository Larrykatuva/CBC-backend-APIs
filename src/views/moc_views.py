from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from src.models.moc_models import Calender, \
    Feedback
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import json


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'


class CreateCalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ('title', 'description', 'fromTimestamp', 'toTimestamp')


class CreateFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'parentId', 'feedbackType', 'feedbackDescription')


class CreateCalenderView(CreateAPIView):
    serializer_class = CreateCalenderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        calender = Calender.objects.create(**data)
        self.serializer_class = CalenderSerializer
        serialized_data = self.serializer_class(calender)
        return Response(data=serialized_data.data, status=status.HTTP_201_CREATED)


class CalenderView(ListAPIView):
    serializer_class = CalenderSerializer
    queryset = Calender.objects.all()

    filterset_fields = ['id', 'title', 'description', 'fromTimestamp', 'toTimestamp']
    ordering_fields = ['id', 'title', 'description', 'fromTimestamp', 'toTimestamp']

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset


class AddFeedback(CreateAPIView):
    serializer_class = CreateFeedbackSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        feedback = Feedback.objects.create(**data)
        serialized_data = self.serializer_class(feedback)
        return Response(data=serialized_data.data, status=status.HTTP_201_CREATED)


class ListFeedbacks(ListAPIView):
    serializer_class = CreateFeedbackSerializer
    queryset = Feedback.objects.all()

    filterset_fields = ['id', 'parentId', 'feedbackType', 'feedbackDescription']
    ordering_fields = ['id', 'parentId', 'feedbackType', 'feedbackDescription']

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset


class GetFeedback(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateFeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter()
