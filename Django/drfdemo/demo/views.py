from rest_framework import status
from rest_framework.views import APIView
from stuapi.models import Student
from demo.serailizers import StudentModelSerializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

"""
GET /demo/students/ 获取学生信息
POST /demo/students/ 添加一个学生信息
GET /demo/students/<PK> 获取一个学生信息
PUT /demo/students/<PK> 更新一个学生信息
DELETE /demo/students/<PK> 删除一个学生信息
"""

"""学习APIView的使用方法"""


# 一般一个类绑定一个url地址
class StudentApiView(APIView):

    def get(self, request):
        """获取所有学生信息"""
        # 1 获取学生列表信息
        student_list = Student.objects.all()
        # 2 实例化序列化器获取序列化对象
        serialers = StudentModelSerializers(instance=student_list, many=True)
        # 3 转换数据返回给客户端
        return Response(serialers.data, status=status.HTTP_200_OK)

    def post(self, request):
        """添加一个数据"""

        # 1 获取客户端提交的数据,实例化序列化器，获取序列化对象
        serialer = StudentModelSerializers(data=request.data)
        # 2 反序列化[验证数据，保存数据到数据库]
        serialer.is_valid(raise_exception=True)
        serialer.save()
        # 3 返回新增的模型数据给客户端
        return Response(serialer.data, status=status.HTTP_200_OK)


class StudentInfoApiView(APIView):
    def get(self, request, pk):
        """获取一条数据"""

        # 1、用pk作为条件获取学生列表信息
        try:
            student = Student.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 2、 实例化序列化器获取序列化对象
        serialer = StudentModelSerializers(instance=student)
        # 3、 转换数据返回给客户端
        return Response(serialer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """更新数据"""
        # 1、用pk作为条件获取学生列表信息
        try:
            student = Student.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 2 获取客户端提交数据
        serialer = StudentModelSerializers(instance=student, data=request.data)
        # 3 反序列化[验证数据和保存数据]
        serialer.is_valid(raise_exception=True)
        serialer.save()
        # 4 返回结果
        return Response(serialer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """删除数据"""
        # 1、用pk作为条件获取数据并且删除
        try:
            student = Student.objects.get(pk=pk).delete()
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 2 返回结果
        return Response({"msg": "OK"}, status=status.HTTP_200_OK)


"""GenericAPIView通用视图类的学习"""


class StudentGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request):
        """获取模型所有信息"""
        # 1、获取模型列表
        instance_queryset = self.get_queryset()  # GenericAPIView 提供方法
        # 2 实例化序列化器获取序列化对象
        serializer = self.get_serializer(instance=instance_queryset)
        # 3 转换数据返回给客户端
        return Response(serializer.data)

    def post(self,request):
        """添加一个数据信息"""
        # 1、获取模型列表提交的数据，实例化序列化器，获取序列化对象

        # 2 反序列化[验证数据，保存到数据库]