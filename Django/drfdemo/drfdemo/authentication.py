from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model

# 自定义认证方式
class CustomerAuthentication(BaseAuthentication):

    def authenticate(self, request):
        user = request.query_params.get("user")
        #   pwd = request.query_params.get("pwd")
        #if user != "root" and pwd != "root":
        #    return None
        #  get_user_model()获取系统用户表用户模型
        user = get_user_model().objects.filter(username=user).first()
        print(user)
        return (user,None)