from django.core.cache import cache
# 创建用户（用户的注册和登录），（超级管理员）查询用户

# 创建用户
import uuid
from rest_framework import status, exceptions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# ListCreateAPIView:可以用于用户的创建和查询
from rest_framework.response import Response

from .auth import UserAuth
from .contants import HTTP_ACTION_LOGIN, HTTP_ACTION_REGISTER
from .models import UserModel
from .permissions import Userpermission
from .serializers import UserSerializer

# 所有用户
# ListCreateAPIView中post用于处理用户创建的【Create()】，


class UsersAPIView(ListCreateAPIView):
    # 序列化类
    serializer_class = UserSerializer
    # 查询集和结果集
    queryset = UserModel.objects.all()
    # 用户验证
    # authentication_classes = (UserAuth,)
    # 权限控制UserAuth
    # permission_classes = (Userpermission,)
    # 直接进行权限控制permission (如上)
    # 重写get请求，判断request.user 是否是UserModel中的一个实例
    # def get(self, request, *args, **kwargs):
    #     if isinstance(request.user, UserModel):
    #         if request.user.is_super:
    #             return self.list(request, *args, **kwargs)
    #         else:
    #             raise exceptions.NotAuthenticated  # 没有超级管理员的权限
    #     else:
    #         raise exceptions.NotAuthenticated   # 用户没有登录，没有权限访问

    # 同一个post做把登录和注册同时完成
    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        # 若参数为register则为注册，创建用户
        if action == HTTP_ACTION_LOGIN:
            return self.create(request, *args, **kwargs)
        elif action == HTTP_ACTION_REGISTER:
            # 验证用户名密码
            employee_number = request.data.get('employee_number')
            print(request.data)
            password = request.data.get('password')
            try:
                user = UserModel.objects.get(employee_number=employee_number)   # 数据库验证用户名
                # 用户名存在验证密码
                if user.password == password:
                    # 生成令牌,传入客户端和放入服务器缓存或者数据库
                    # token = uuid.uuid4().hex
                    # 把token放入缓存,注意Redis在settings中的配置
                    # cache.set(token, user.id)
                    # 并传入客户端
                    data = {
                        'msg': 'ok',
                        'status': 200,
                        # 'token': token
                    }
                    return Response(data)
                else:
                    raise exceptions.AuthenticationFailed   # 用户密码错误
            except UserModel.DoesNotExist:
                raise exceptions.NotFound   # 用户名错误
        else:
            raise exceptions.ValidationError  # 验证错误，传入的不是POST请求

    # 创建用户
    # 重写的CreateModelMixin中的方法：用于用户的创建
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     data = serializer.data
    #     u_name = data.get('u_name')
    #     # 判断是否是创建的超级用户
    #     if u_name in SUPER_USERS:
    #         u_id = data.get('id')
    #         user = UserModel.objects.get(pk=u_id)  # 拿到对应的用户
    #         user.is_super = True  # 设置为超级用户o0
    #         user.save()
    #         data.update({'is_super': True})     # 创建了超级用户，在返回客户端的时候也把对应修改做了
    #
    #     headers = self.get_success_headers(data)
    #     return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# 单个用户,只用于展示
class UserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()