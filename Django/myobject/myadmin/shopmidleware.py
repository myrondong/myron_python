# 自定义中间类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse
import re


class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:", path)

        # 判断管理后台是否登录
        # 定义后台不登录也可直接访问的url列表
        ulist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin']
        # 判断当前请求url地址是否是以/myadmin开头,并且不在urllist中，才做是否登录判断
        if re.match(r'^/myadmin', path) and path not in ulist:
            print(request.session)
            # 判断登录（key 名为adminuser是否存在session中）
            if 'adminuser' not in request.session:
                return redirect(reverse("myadmin_login_index"))
                # pass

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
