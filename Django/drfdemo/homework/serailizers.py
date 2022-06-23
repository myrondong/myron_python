from rest_framework import serializers
from homework.models import HomeWork
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = "__all__"