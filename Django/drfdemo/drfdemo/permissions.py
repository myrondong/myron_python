from rest_framework.permissions import BasePermission

class IsXiaoMingPermission(BasePermission):
    """
    自定义权限，可以全局和局部配置
    局部配置：放到视图类里面
    全局配置：放到类似drfdemo这样文件夹里面
    """
    def has_permission(self, request, view):
        """
        视图权限
        返回结果未True表示允许访问视图类
        request：本次客户端提交请求对象
        view：本次客户端访问视图类
        """
        # user = request.query_params.get("user")

        # return user=="dll"

        return bool(request.user and request.user.username == "dll")

    # 两者不可兼容
    # def has_object_permission(self, request, view, obj):
    #     """
    #     模型权限：写了视图权限(has_permisson)方法
    #     一般不写这个返回结果
    #     True表示允许操作
    #
    #     request: 本次客户端请求处理对象
    #     view： 本次客户端请求视图对象
    #     obj: 本次权限判断的模型对象
    #     """
    #     from school.models import Student
    #     if isinstance(obj,Student):
    #         user = request.query_name.get("user")
    #         return user == "dll"
    #     else:
    #
    #         return True