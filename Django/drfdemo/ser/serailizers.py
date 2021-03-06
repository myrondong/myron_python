from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from stuapi.models import Student

"""
serializers 是drf 提供给开发者调用序列化模块
面声明所有可以序列化器的基类，其中
serializer 序列化基类，drf 所有序列化器都必须继承 serializer
ModelSerializer 模型序列化器，是序列化器的子类，除了serializer，最常用序列化器

序列化器作用 Serializers：
1、序列化会把模型对象转换成字典，经过response变成json
2、反序列化把客户端发送过来数据，经过request变成字典，序列化器可以把字典转化成模型
3、反序列化，完成数据校验功能

模型序列化器 ModelSerializer:
1、基于模型类自动生成一些列字段
2、基于模型类自动Serializers和validators,比如unique_together -> 联合索引
2、包含默认的create()和update()的实现
"""


def check_classmate(data):
    """外部函数验证"""
    if len(data) < 3:
        raise serializers.ValidationError(detail='班级格式不对', code='check classmate')
    # 验证完成返回结果
    return data


class StudentSerializers(serializers.Serializer):
    # 学生序列化器
    # 1、转换字段声明
    # 客户端字段 = serializers.字段类型(选项=选项值，)
    id = serializers.IntegerField(read_only=True)  # read_only=True 反序列化中不会要求id 有值
    name = serializers.CharField(required=True)  # required=True 反序列化阶段必填
    sex = serializers.BooleanField(default=True)  # default=True 没有数据时候默认true
    age = serializers.IntegerField(max_value=99, min_value=0, error_messages={"min_value": "The Fail",
                                                                              "max_value": "Fial"})  # max_value=99,min_value=0 反序列化 o<=x =99
    description = serializers.CharField(allow_null=True, allow_blank=True)  # 允许为空{None}或者数据为""
    classmate = serializers.CharField(validators=[check_classmate])  # validators 外部验证函数值选项是一个列表，列表得到成员函数名，不能字符串。

    # 2、如果字段当前序列化器继承ModelSerializer，则需要声明调用的模型信息
    # class Meta:
    #    model = Student
    #    fields = "__all__"
    #    fields = ['id','name'] # 还可以写成
    # 3、验证代码对象方法
    def validate(self, attrs):  # validate名称固定的
        """验证客户端所有数据
        类似注册会员密码和确认密码只能在validate验证
            validate是固定方法
            参数 attrs，是序列化器实例化时候data选项数据
        """
        if attrs['age'] < 0:
            raise serializers.ValidationError(detail='年龄不对')
        print(f'attrs={attrs}')
        return attrs

    def validate_name(self, data):  # 方法名格式必须validate_<字段>为序列化器，否则序列化器无法识别
        """验证单个字段
        方法名称必须是validate_<字段名> 为名称，否则序列化不识别
        validate开头方法会被，自动被is_valid调用
        """
        print(f'name = {data}')
        if data in ['python', 'django']:
            # 在序列化器中，验证失败可以通过异常方式告知is_valid
            raise serializers.ValidationError(detail='学生姓名不在这里')
        # 验证成功后返回数据
        return data

    # 4、模型操作方法(create ,update)
    def create(self, validated_data):
        """
        完成添加操作，添加数据以后，就自动从字典变成模型对象过程
        方法固定create,参数固定validated_data就是验证成功后的结果，
        就是自动从字典对象变成模型对象的一个过程
        :param validated_data:
        :return:
        """
        instance = Student.objects.create(**validated_data)
        # serlizers = StudentSerializers(instance=instance)
        return instance

    def update(self, instance, validated_data):
        """
        完成更新操作，更新数据以后，就自动从字典变成模型对象过程
        方法固定名称 update
        :param instance:固定参数，实例化序列化对象时，必须传入模型对象
        :param validated_data:固定参数，，验证成功后的结果
        :return:更新数据后，就自动实现从字典变成模型对象的过程
        """
        # print(f"instance : {instance}")
        # instance.name = validated_data['name']
        # instance.age = validated_data['age']
        # instance.sex = validated_data['sex']
        # instance.classmate = validated_data['classmate']
        # instance.description = validated_data['description']
        # print(instance.classmate,instance.description)
        for key, value in validated_data.items():
            # setattr 设置对象属性作用
            setattr(instance, key, value)
        instance.save()
        # 调用模型对象的save方法和视图serialzier.save()不是同一种方法
        return instance


class StudentSerializers1(serializers.Serializer):
    # 学生序列化器
    # 1、转换字段声明
    # 客户端字段 = serializers.字段类型(选项=选项值，)
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    description = serializers.CharField()

    # 2、如果字段当前序列化器继承ModelSerializer，则需要声明调用的模型信息
    # class Meta:
    #    model = Student
    #    fields = "__all__"
    #    fields = ['id','name'] # 还可以写成
    # 3、验证代码对象方法
    # def validate(self, attrs): # validate名称固定的
    #    pass
    #    return attrs

    # def validate_<字段>(self, data): # 方法名格式必须validate_<字段>为序列化器，否则序列化器无法识别
    #   pass
    #   return data

    # 4、模型操作方法(create ,update)
    # def create(self, validated_data):
    #   完成添加操作，添加数据以后，就自动从字典变成模型对象过程
    #    pass

    # def update(self, instance, validated_data):
    #   完成更新操作，更新数据以后，就自动从字典变成模型对象过程
    #    pass

# 一把全部从数据库提取数据用ModelSerializer 简单
class StudentModelSerializer(serializers.ModelSerializer):
    """学生模型序列化器"""

    # 1、转换的字段说明
    # 字段名 = 字段类型(选项=选项值)
    nickname = serializers.CharField(default="BCD",read_only=True)

    # 2、如果字段当前序列化器继承ModelSerializer，则需要声明调用的模型信息
    # class Meta 必须两个属性model，fields
    class Meta:
        model = Student
        fields = "__all__"
        #fields = ['name', 'sex', 'age', 'classmate', 'description','nickname']
        #    read_only_fields = [] # 选填，只读字段序列，表示设置这里字段只会在序列化阶段采用
        #    fields = ['id','name'] # 还可以写成
        extra_kwargs = {  # 选填字段额外选项
            "age": {
                "min_value": 0,
                "max_value": 20,
                "error_messages": {
                    "age": {
                        "min_value": "aa",
                        "max_value": "bb"
                    }
            },
            }
        }

    # 3、验证代码对象方法
    # def create(self, validate_data):
    #     # 密码加密
    #     validate_data['password'] = make_password(validate_data['password'])
    #
    #     pass

    # 4、模型操作方法(create ,update)
