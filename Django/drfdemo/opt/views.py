from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from drfdemo.authentication import CustomerAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

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
    permission_classes = [IsAdminUser] # 当前视图所有方法必须只能被
    def get(self, request):
        print(request.user.id)
        if request.user.id:
            print("通过认证")
        else:
            print("没有通过认证")
        return Response({"msg": 'OK'})
