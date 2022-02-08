import hashlib
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from myadmin.models import User


# Create your views here.
# 后台管理首页
def index(request):
    return render(request, 'myadmin/index/index.html')


# 管理员登录表单
def login(request):
    return render(request, 'myadmin/index/login.html')


# 执行管理员登录
def dologin(request):
    try:
        user = User.objects.get(username=request.POST['username'])
        # 判断是否管理员

        if user.status == 6:
            md5 = hashlib.md5()
            s = request.POST['password'] + user.password_salt  # 从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
            if user.password_hash == md5.hexdigest():  # 获取md5值
                print('登录成功')
                request.session['adminuser'] = user.toDict()
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info': '密码的登录错误'}
        else:
            context = {'info': '无效的登录账号'}

    except Exception as e:
        context = {'info': '账号不存在'}
        print(e)
    return render(request, 'myadmin/index/login.html', context)


# 管理员退出
def logout(request):
    pass
