from rest_framework.serializers import ModelSerializer

from school.models import Teacher, Student


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model=Teacher
        fields = "__all__"

class StudentModelSerializer(ModelSerializer):
    class Meta:
        model=Student
        fields = "__all__"