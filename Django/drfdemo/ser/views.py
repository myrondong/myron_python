from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from stuapi.models import Student
# Create your views here.
from .serailizers import StudentSerializers
import json


class StudentView(View):
    def get1(self, requests):
        """序列化器-序列化调用-序列化一个模型调用"""
        # 0、获取数据集
        students = Student.objects.first()

        # 1、实例化序列化器，得到序列化对象
        sers = StudentSerializers(instance=students)

        datas = sers.data
        # 3、相应数据
        # json_dumps_params 把json转字典 意义不大

        return JsonResponse(data=datas, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    def get2(self, requests):
        """序列化器使用-调用阶段 序列化多个模型对象"""
        # 0、获取数据集
        stu_list = Student.objects.all()

        # 1、实例化序列化器，得到序列化对象
        # 如何序列化多个[务必使用many=True]

        sers = StudentSerializers(instance=stu_list, many=True)
        # 2、调用实列化对象的data属性方法获取转换后数据

        datas = sers.data
        # 3、相应数据
        # json_dumps_params 把json转字典 意义不大

        return JsonResponse(data=datas, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    def get3(self, requests):
        """反序列化-采用字段选项验证数据[验证失败抛出异常，工作中最常用]"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "xiaowang",
            "age": 110,
            "sex": True,
            "classmate": "2200",
            "description": '"12121d'
        }
        # 1.1 实例化对象，获取实例化对象
        sers = StudentSerializers(data=data)
        # 1.2 调用序列化器进行验证数据
        ret =sers.is_valid() # 不抛出异常
        # ret = sers.is_valid(raise_exception=True)  # 抛出异常

        print(ret)
        if ret:
            a = sers.validated_data
            print(a)
            return JsonResponse(dict(sers.validated_data))
        else:
            print(sers.error_messages)
            return JsonResponse(dict(sers.errors))
        # 1.3 获取到验证的结果
        # 2、操作数据库
        # 3、返回结果
        return JsonResponse({})

    def get(self, requests):
        """反序列化-采用字段选项验证数据[验证失败抛出异常]"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "xiaowang",
            "age": 110,
            "sex": True,
            "classmate": "2200",
            "description": '"12121d'
        }
        # 1.1 实例化对象，获取实例化对象
        sers = StudentSerializers(data=data)
        # 1.2 调用序列化器进行验证数据
        # ret =sers.is_valid() # 不抛出异常
        sers.is_valid(raise_exception=True)  # 抛出异常，代码不会执行下来

        return JsonResponse(dict(sers.validated_data))

        # 1.3 获取到验证的结果
        # 2、操作数据库
        # 3、返回结果
        return JsonResponse({})
