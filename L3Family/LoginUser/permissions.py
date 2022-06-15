from rest_framework.permissions import BasePermission

from .models import UserModel


class Userpermission(BasePermission):
    # 重写方法，进行权限限制
    def has_permission(self, request, view):
        # 针对get请求的权限控制
        if request.method == 'GET':
            # 在用户存在的情况下
            if isinstance(request.user, UserModel):
                # 用户是超级用户返回True
                return request.user.user_level
            return False
        return True