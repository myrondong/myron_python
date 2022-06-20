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
        return Response(serialer.data, status=status.HTTP_201_CREATED)


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
        serializer = self.get_serializer(instance=instance_queryset, many=True)
        # 3 转换数据返回给客户端
        return Response(serializer.data)

    def post(self, request):
        """添加一个数据信息"""
        # 1、获取模型列表提交的数据，实例化序列化器，获取序列化对象
        serializer = self.get_serializer(data=request.data)
        # 2 反序列化[验证数据，保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3 返回数据给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentInfoGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request, pk):
        """获得一个数据"""
        # 1、用pk作为条件获取模型对象
        instance = self.get_object()
        # 2、 实例化序列化器获取序列化对象
        serializer = self.get_serializer(instance=instance)
        # 3、 转换数据返回给客户端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """更新一个数据"""
        # pk request 参数不可以省
        # 1、用pk作为条件获取模型对象
        instance = self.get_object()
        # 2、获取客户端数据
        serializer = self.get_serializer(instance=instance, data=request.data)
        # 3 反序列化[验证数据和保存数据]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4 转换数据返回给客户端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """删除数据"""
        # 1、用pk作为条件获取数据并且删除
        self.get_object().delete()
        # 2 返回结果
        return Response({"msg": "OK"}, status=status.HTTP_200_OK)


"""
from rest_framework.mixins import ListModelMixin  
获取多条数据返回结果 List

from rest_framework.mixins import CreateModelMixin  
添加一条数据返回结果 create

from rest_framework.mixins import RetrieveModelMixin 
获取一条数据返回响应结果 retrieve

from rest_framework.mixins import UpdateModelMixin 
更新一条数据返回响应结果 update(更新全部字段)和partial_update(跟新单个或者部分字段，例如修改密码，头像)

from rest_framework.mixins import DestroyModelMixin
删除一条数据返回响应结果 destory
"""

from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin


class StudentMixinsAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request):
        """获取所有数据"""
        return self.list(request)

    def post(self, request):
        """跟新数据"""
        return self.create(request)


from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin


class StudentInfoMixinsAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get(self, request, pk):
        """获取一个数据"""
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """更新一个数据"""
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


"""
较上图的代码更加精简 drf 在使用GenericAPIView和Mixins进行组合以后还提供的视图子类
视图子类是通用模型类和模型扩展类的子类
ListApiView = ListModelMixin + GenericAPIView           获取多条数据返回结果
CreateApiView = CreateModelMixin + GenericAPIView       添加一条数据返回结果
RetrieveApiView = RetrieveModelMixin + GenericAPIView   获取一条数据返回结果
UpdateApiView = UpdateModelMixin + GenericAPIView       更新一条数据返回结果
DestroyApiView = DestroyModelMixin + GenericAPIView     删除一条数据返回结果

-> 组合视图子类
ListCreateApiView = ListApiView + CreateApiView
RetrieveUpdateApiView = RetrieveApiView + UpdateApiView
RetrieveDestroyApiView = RetrieveApiView + DestroyApiView
RetrieveUpdateDestroyApiView = RetrieveApiView + DestroyApiView +UpdateApiView
"""

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView


class StudentView(ListAPIView, CreateAPIView):
    queryset = Student.objects.all()
    # 假如想修改里面数据那就写get 方法，就是继承父类的一些信息
    serializer_class = StudentModelSerializers


class StudentInfoView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers


"""
上述代码依然重复问题
1、路由重复问题
2、get方法重复问题
drf 提供视图集 ViewSet
ViewSet -->  基本视图集                   APIView中代码重复问题
GenericViewSet --> 通用视图集    解决APIView中代码重复问题，同时让代码更通用
"""
from rest_framework.viewsets import ViewSet


# 基本视图集
class StudentViewSet(ViewSet):
    def get_list(self, request):
        """获取所有学生信息"""
        # 1 获取学生列表信息
        student_list = Student.objects.all()
        # 2 实例化序列化器获取序列化对象
        serialers = StudentModelSerializers(instance=student_list, many=True)
        # 3 转换数据返回给客户端
        return Response(serialers.data, status=status.HTTP_200_OK)

    def create_student(self, request):
        """添加一个数据"""
        # 1 获取客户端提交的数据,实例化序列化器，获取序列化对象
        serialer = StudentModelSerializers(data=request.data)
        # 2 反序列化[验证数据，保存数据到数据库]
        serialer.is_valid(raise_exception=True)
        serialer.save()
        # 3 返回新增的模型数据给客户端
        return Response(serialer.data, status=status.HTTP_201_CREATED)

    def get_one_sutdent(self, request, pk):

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

    def update_student(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialer = StudentModelSerializers(instance=student, data=request.data)
        # 3 反序列化[验证数据和保存数据]
        serialer.is_valid(raise_exception=True)
        serialer.save()
        # 4 返回结果
        return Response(serialer.data, status=status.HTTP_200_OK)

    def delet_one_student(self, request, pk):

        try:
            student = Student.objects.all(pk=pk).delete()
        except:
            Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"msg": "OK"}, status=status.HTTP_200_OK)


# 通用视图集
from rest_framework.viewsets import GenericViewSet


class StudentGenericViewSet(GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

    def get_student_list(self, request):
        """获取模型所有信息"""
        # 1、获取模型列表
        instance_queryset = self.get_queryset()  # GenericAPIView 提供方法
        # 2 实例化序列化器获取序列化对象
        serializer = self.get_serializer(instance=instance_queryset, many=True)
        # 3 转换数据返回给客户端
        return Response(serializer.data)

    def create(self, request):
        """添加一个数据信息"""
        # 1、获取模型列表提交的数据，实例化序列化器，获取序列化对象
        serializer = self.get_serializer(data=request.data)
        # 2 反序列化[验证数据，保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3 返回数据给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """获得一个数据"""
        # 1、用pk作为条件获取模型对象
        instance = self.get_object()
        # 2、 实例化序列化器获取序列化对象
        serializer = self.get_serializer(instance=instance)
        # 3、 转换数据返回给客户端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        """更新一个数据"""
        # pk request 参数不可以省
        # 1、用pk作为条件获取模型对象
        instance = self.get_object()
        # 2、获取客户端数据
        serializer = self.get_serializer(instance=instance, data=request.data)
        # 3 反序列化[验证数据和保存数据]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4 转换数据返回给客户端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_student(self, request, pk):
        try:
            student = Student.objects.all(pk=pk).delete()
        except:
            Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"msg": "OK"}, status=status.HTTP_200_OK)


# 通用视图集 + 混入类
class StudentMixinsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                           DestroyModelMixin):
    queryset = Student.objects.all()
    # 假如想修改里面数据那就写get 方法，就是继承父类的一些信息
    serializer_class = StudentModelSerializers


"""
上面接口继承父类太多了
我们继续让一些合并的父类让视图继承即可
ReadOnlyModelViewSet = GenericViewSet + mixins.RetrieveModelMixin + mixins.ListModelMixin, 
ModelViewSet 实现五个api接口    
"""
from rest_framework.viewsets import ReadOnlyModelViewSet


class StudentReadOnlyModelViewSet(ReadOnlyModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    # 假如想修改里面数据那就写get 方法，就是继承父类的一些信息
    serializer_class = StudentModelSerializers


from rest_framework.viewsets import ModelViewSet


# 最简便版本了
class StudentModelViewSet(ModelViewSet): # 万能视图 最常用的这个类
    queryset = Student.objects.all()
    # 假如想修改里面数据那就写get 方法，就是继承父类的一些信息
    serializer_class = StudentModelSerializers
