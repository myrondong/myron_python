from rest_framework import serializers
from stuapi.models import Student


class StudentModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['id','name'] # 还可以写成
