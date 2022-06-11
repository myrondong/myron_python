from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from LoginUser.models import User


# 注册
class RegSerializers(serializers.ModelSerializer):
    pwd_validate = serializers.CharField(max_length=256, min_length=4, write_only=True)
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = User
        # fields = ('username', 'password', 'pwd_validate', 'tel','employee_num')
        fields = "__all__"

    def validate(self, attrs):

        if attrs['pwd_validate'] != attrs['password']:
            raise ValidationError('两次密码输入不一致')
        del attrs['pwd_validate']
        # 对密码进行加密 make_password
        attrs['password'] = make_password(attrs['password'])
        return attrs
    # 登录


class LogSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=16)
    employee_num = serializers.CharField(max_length=7)
    class Meta:
        model = User
        fields = ('employee_num', 'password')

    def validate(self, attrs):
        user_obj = User.objects.filter(username=attrs['employee_num']).first()
        if user_obj:
            # check_password　可以将加密后的密码与输入的密码进行对比
            if check_password(attrs['password'], user_obj.password):
                return attrs
        raise ValidationError('工号或密码错误')
