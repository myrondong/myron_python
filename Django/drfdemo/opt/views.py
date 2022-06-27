from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from drfdemo.authentication import CustomerAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from drfdemo.permissions import IsXiaoMingPermission
from school.models import Student

"""
学习权限
认证
限流
过滤
分页
异常处理
"""

class ExampleView(APIView):
    # 验证
    # 局部调用
    # 认证
    authentication_classes = [CustomerAuthentication, ]

    def get(self, request):
        print(request.user.id)
        if request.user.id is None:
            print("通过认证")
        else:
            print("没有通过认证")
        return Response({"msg": 'OK'})


class HomeView(APIView):
    # permission_classes = [IsAuthenticated,] # 当前视图所有方法，只能被已经登录的站点会员访问
    # permission_classes = [IsAdminUser] # 当前视图所有方法必须只能被站点管理员访问 user.is_staff 为真时候
    permission_classes = [IsXiaoMingPermission]  # 当前视图所有方法必须游客访问，可以查看数据但是不能修改数据

    def get(self, request):
        print(request.user.id)
        if request.user.id:
            print("通过认证")
        else:
            print("没有通过认证")
        return Response({"msg": 'OK'})


from rest_framework.generics import RetrieveAPIView
from school.serailizers import StudentModelSerializer
from rest_framework.throttling import UserRateThrottle


class StudentInfoApiView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [IsXiaoMingPermission]
    throttle_classes = [UserRateThrottle]


class Demo1APiView(APIView):
    """
    自定义限流
    """
    permission_classes = [IsAuthenticated]
    throttle_scope = 'member'

    def get(self, request):
        return Response({"msg": 'OK'})


class Demo2APiView(APIView):
    """
    自定义限流
    """
    permission_classes = [IsAuthenticated]
    throttle_scope = 'vip'

    def get(self, request):
        return Response({"msg": 'OK'})


class Demo3APiView(APIView):
    """
    自定义限流
    """
    permission_classes = [IsAuthenticated]
    throttle_scope = 'vvip'

    def get(self, request):
        return Response({"msg": 'OK'})


from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from stuapi.models import Student
from students.serailizers import StudentModelSerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class Demo4APiView(ListAPIView, RetrieveUpdateDestroyAPIView):
    """
    过滤查询
    """
    # 过滤话局部会覆盖全局配置
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # 局部配置
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    # http://127.0.0.1:8000/opt/demo4/?sex=true 查找sex = 男的
    # http://127.0.0.1:8000/opt/demo4/?age=10   查找年纪10
    # http://127.0.0.1:8000/opt/demo4/?age=10&sex=true   男的查找年纪10
    # 分类
    filter_fields = ['sex', 'age']
    # http://127.0.0.1:8000/opt/demo4/?odering=id id进行排序从小到大
    # http://127.0.0.1:8000/opt/demo4/?odering=id 从大到小

    # list 方法中调用-》GenericAPIView 中 filter_queryset 方法 ----》配置过略器
    # 的filter_queryset ---》filter_fields
    # 排序
    ordering_fields = ['id', 'sex']


# 分页
from rest_framework.pagination import PageNumberPagination

class StudentPageNumberPagination(PageNumberPagination):
    page_size_query_param='size' # 查询字符串代表每一页变量名
    page_query_param='page' #查询字符串页码的变量名称
    page_size = 2 # 每页数据量
    max_page_size = 4 # 允许客户通过客户端查询字符串的最大单页数据

class Demo5APiView(ListAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    # 局部分页
    # pagination_class =None 关闭全局分页影响
    # 局部分页往往采用自定义分页类，进行分页数据量配置

    # 局部配置分页功能
    # http://127.0.0.1:8000/opt/demo5/?page=2&size=5
    pagination_class = StudentPageNumberPagination


class Demo6APiView(APIView):
    def get(self, request):
        1/0
        return Response({"msg": 'OK'})