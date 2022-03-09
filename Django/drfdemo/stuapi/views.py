import json

from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Student
from django.http.response import JsonResponse


class StudentsView(View):
    """学生视图"""
    def post(self, request):
        """添加学生"""
        # 1、接受客户提交数据
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        classmate = request.POST.get('classmate')
        description = request.POST.get('description')

        print(description)

        # 1.1 客户验证数据
        instance = Student.objects.create(
            name=name,
            sex=sex,
            age=age,
            classmate=classmate,
            description=description
        )
        # 1.2 操作数据库，保存数据

        # 返回结果
        return JsonResponse(data={
            "id": instance.pk,
            "name": instance.name,
            "sex": instance.sex,
            "age": instance.age,
            "classmate": instance.classmate,
            "description": instance.description
        }, status=201)


    def get(self,request):
        """查询学生信息"""
        students_list = Student.objects.all()
        return JsonResponse(students_list,status=200,safe=False)

class StudentInfo(View):
    def get(self,request,pk):
        try:
            instance = Student.objects.get(pk=pk)
            print(pk)
            return JsonResponse(data={
                "id": instance.pk,
                "name": instance.name,
                "sex": instance.sex,
                "age": instance.age,
                "classmate": instance.classmate,
                "description": instance.description
            },status=200)
        except Exception as e:
            return JsonResponse(data={},status=404)

    def put(self,request,pk):
        data = json.loads(request.body)
        name = data.get('name')
        sex = data.get('sex')
        age = data.get('age')
        classmate = data.get('classmate')
        description = data.get('description')
        try:
            instance = Student.objects.get(pk=pk)
            print(pk)
            instance.name = name
            instance.sex =sex
            instance.age =age
            instance.classmate =classmate
            instance.description =description
            instance.save()

        except Exception as e:
            return JsonResponse(data={},status=404)

        return JsonResponse(data={
            "id": instance.pk,
            "name": instance.name,
            "sex": instance.sex,
            "age": instance.age,
            "classmate": instance.classmate,
            "description": instance.description
        }, status=200)

    def delete(self,request,pk):
        """删除一个学生信息"""
        try:
            Student.objects.filter(pk=pk).delete()
        except Exception as e:
            pass
        return JsonResponse(data={},status=204)