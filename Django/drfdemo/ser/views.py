from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from stuapi.models import Student
from ser.serailizers import StudentSerializers, StudentModelSerializer # Alt+Enter自动导包
import json

# Create your views here.

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
            "age": 10,
            "sex": True,
            "classmate": "2200",
            "description": '"12121d'
        }
        # 1.1 实例化对象，获取实例化对象
        sers = StudentSerializers(data=data)
        # 1.2 调用序列化器进行验证数据
        ret = sers.is_valid()  # 不抛出异常
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

    def get4(self, requests):
        """反序列化-采用字段选项验证数据[验证失败抛出异常]"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "xiaowang",
            "age": 10,
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

    def get5(self, requests):
        """反序列化-验证完成以后，添加数据"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "xiaowang66",
            "age": 10,
            "sex": True,
            "classmate": "2200",
            "description": '"12121d'
        }
        # 1.1 实例化对象，获取实例化对象
        sers = StudentSerializers(data=data)

        # 1.2 调用序列化器进行验证数据
        sers.is_valid(raise_exception=True)  # 抛出异常，代码不会执行下来

        # 1.3 获取到验证的结果
        # data = sers.validated_data
        # print(data)

        # 2、操作数据库
        # instance = Student.objects.create(**sers.validated_data)
        # serlizers = StudentSerializers(instance=instance)
        sers.save()
        # 会根据实例化序列化器时候，是否传入instance属性来自动调用create或者update方法，传入instance属性
        # 自动调用update方法；没有传入instance属性会自动调用create

        # 3、返回结果
        return JsonResponse(data=sers.data, status=200)

    def get(self, requests):
        """反序列化-验证完成以后，更新数据"""
        # 1、根据客户端访问的url地址，获取pk值
        # ser/students/2/ path("students/?P<pk>\d+",views.StudentView.as_view())
        pk = 1
        try:
            student = Student.objects.get(pk=pk)
            print(f"student object:{student}")
        except Exception as e:
            return JsonResponse({"error": "当前学生不存在"}, status=404)
        # 2、接受客户提交
        # 模拟数据
        data = {
            "name": "11xiaowang66",
            "age": 20,
            "sex": True,
            "classmate": "2200",
        }
        # 3、修改操作中的实例化序列化对象
        # serial = StudentSerializers(instance=student, data=data)
        serial = StudentSerializers(instance=student, data=data,partial=True)
        # partial=True 这个表示需要修改部分data数据

        # 4.验证数据
        serial.is_valid(raise_exception=True)
        # 5.入库
        # request.user 是django 中记录登录用户的模型数据
        serial.save() # 在save中，传递一些不需要验证的数据到模型里面
        # 6。返回结果
        return JsonResponse(data=serial.data, status=200)


class StudentModelView(View):
    """模型序列化器"""
    def get1(self, requests):
        """序列化器-序列化调用-序列化一个模型调用"""
        # 0、获取数据集
        students = Student.objects.first()
        students.nickname ='小学生'
        # 1、实例化序列化器，得到序列化对象
        sers = StudentModelSerializer(instance=students)

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

        sers = StudentModelSerializer(instance=stu_list, many=True)
        # 2、调用实列化对象的data属性方法获取转换后数据

        datas = sers.data
        # 3、相应数据
        # json_dumps_params 把json转字典 意义不大

        return JsonResponse(data=datas, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    def get(self, requests):
        """反序列化-采用字段选项验证数据[验证失败抛出异常，工作中最常用]"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "11xiaowang",
            "age": 10,
            "sex": True,
            "classmate": "2200",
            "description": '"12121d'
        }
        # 1.1 实例化对象，获取实例化对象
        sers = StudentModelSerializer(data=data)
        # 1.2 调用序列化器进行验证数据
        ret = sers.is_valid()  # 不抛出异常
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

    def get4(self, requests):
        """反序列化-采用字段选项验证数据[验证失败抛出异常]"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "xiaowang",
            "age": 10,
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

    def get5(self, requests):
        """反序列化-验证完成以后，添加数据"""
        # 1、接受客户提交
        # data = json.dumps(requests.body)
        # 模拟数据
        data = {
            "name": "xiaowang66",
            "age": 10,
            "sex": True,
            "classmate": "2200",
            "description": '"12121d'
        }
        # 1.1 实例化对象，获取实例化对象
        sers = StudentSerializers(data=data)

        # 1.2 调用序列化器进行验证数据
        sers.is_valid(raise_exception=True)  # 抛出异常，代码不会执行下来

        # 1.3 获取到验证的结果
        # data = sers.validated_data
        # print(data)

        # 2、操作数据库
        # instance = Student.objects.create(**sers.validated_data)
        # serlizers = StudentSerializers(instance=instance)
        sers.save()
        # 会根据实例化序列化器时候，是否传入instance属性来自动调用create或者update方法，传入instance属性
        # 自动调用update方法；没有传入instance属性会自动调用create

        # 3、返回结果
        return JsonResponse(data=sers.data, status=200)

    def get6(self, requests):
        """反序列化-验证完成以后，更新数据"""
        # 1、根据客户端访问的url地址，获取pk值
        # ser/students/2/ path("students/?P<pk>\d+",views.StudentView.as_view())
        pk = 1
        try:
            student = Student.objects.get(pk=pk)
            print(f"student object:{student}")
        except Exception as e:
            return JsonResponse({"error": "当前学生不存在"}, status=404)
        # 2、接受客户提交
        # 模拟数据
        data = {
            "name": "11xiaowang66",
            "age": 120,
            "sex": True,
            "classmate": "2200",
        }
        # 3、修改操作中的实例化序列化对象
        # serial = StudentSerializers(instance=student, data=data)
        serial = StudentSerializers(instance=student, data=data,partial=True)
        # partial=True 这个表示需要修改部分data数据

        # 4.验证数据
        serial.is_valid(raise_exception=True)
        # 5.入库
        # request.user 是django 中记录登录用户的模型数据
        serial.save() # 在save中，传递一些不需要验证的数据到模型里面
        # 6。返回结果
        return JsonResponse(data=serial.data, status=200)
