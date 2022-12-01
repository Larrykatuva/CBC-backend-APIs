from src.models.school_models import Child, ChildInstance, Grade, Subject, Feed
from src.services.child_instance_service import ChildInstanceService
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    """Subject serializer"""
    class Meta:
        model = Subject
        fields = ('id', 'subject_title', 'status', 'course', 'color', 'abbreviation')


class StrandSerializer(serializers.Serializer):
    """Strand serializer schema to be nested in learning area serializer"""
    strand = serializers.CharField(allow_null=True)
    average = serializers.FloatField()

    class Meta:
        fields = ('strand', 'average')


class LearningAreaSerializer(serializers.Serializer):
    """Learning area report serializer"""
    learning_area = serializers.CharField(allow_null=True)
    average = serializers.FloatField()
    strand = StrandSerializer(many=True)

    class Meta:
        fields = ('learning_area', 'average', 'strand')


class CreateChildInstanceSerializer(serializers.ModelSerializer):
    """Create child instance serializer data schema"""
    class Meta:
        model = ChildInstance
        fields = ('child', 'grade')

    def validate(self, attrs):
        """Custom serializer validation"""
        child = attrs.get('child')
        grade = attrs.get('grade')

        if ChildInstanceService.filter_child_instances({
            "child": child, "grade": grade
        }).__len__() > 0:
            raise serializers.ValidationError(
                detail={'instance': ['Instance combination already exists']},
                code=400
            )
        return attrs


class UpdateChildInstanceSerializer(serializers.ModelSerializer):
    """Update child instance serializer data schema"""
    class Meta:
        model = ChildInstance
        fields = ('child', 'grade')


class ChildSerializer(serializers.ModelSerializer):
    """Child serializer to be nested in Child instance serializers"""
    class Meta:
        model = Child
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    """Grade serializer to be nested in child serializers"""
    class Meta:
        model = Grade
        fields = '__all__'


class ReadChildInstanceSerializer(serializers.ModelSerializer):
    """Read child instance serializer data schema"""
    child = ChildInstance()
    grade = GradeSerializer()

    class Meta:
        model = ChildInstance
        fields = ('id', 'created_at', 'updated_at', 'child', 'grade')



