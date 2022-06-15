# serializers.py
# 用户序列化
from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # 要显示出来的字段
        fields = ('id', 'employee_number','name','password', 'email', 'phone')
