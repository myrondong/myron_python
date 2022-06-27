from rest_framework import serializers
from stuapi.models import Student


class StudentModelSerializers1(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = "__all__"
        extra_kwargs={
            "age":{
                "max_value":100,
                "error_messages":{
                    "max_value":"不能超过100岁"

                }

            }
        }