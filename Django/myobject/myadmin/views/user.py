# 员工视图文件
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import hashlib
import random


def index(request, p_index=1):
    """浏览信息"""

    umod = User.objects
    list_mod = umod.filter(status__lt=9)
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    my_where = []
    if kw:
        list_mod = list_mod.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        my_where.append('keyword=' + kw)

    status = request.GET.get("status", '')
    if status != '':
        list_mod2 = list_mod.filter(status=status)
        my_where.append('status=' + status)
    # 执行分页( •̀ ω •́ )处理
    p_index = int(p_index)
    page = Paginator(list_mod, 5)  # 每页五条显示
    max_page = page.num_pages
    if p_index > max_page:
        p_index = max_page
    elif p_index < 1:
        p_index = 1
    list_mod2 = page.page(p_index)  # 获取当前页数据
    p_list = page.page_range  # 获取页码列表信息
    context = {"user_list": list_mod2, 'p_list': p_list, 'p_index': p_index, 'max_pages': max_page,
               'my_where': my_where}
    print(context)
    return render(request, 'myadmin/user/index.html', context)


def add(request):
    """加载信息添加表单"""
    return render(request, 'myadmin/user/add.html')


def insert(request):
    """执行信息添加"""
    try:
        ob = User()
        # 将当前员工信息的密码做md5处理
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n)  # 从表单中获取密码并添加干扰值
        md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
        ob.password_hash = md5.hexdigest()  # 获取md5值
        ob.password_salt = n
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        ob.status = 1
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '添加成功'}
    except Exception as err:
        context = {'info': '添加失败'}
        print(err)
    return render(request, 'myadmin/info.html', context)


def delete(request, uid=0):
    """执行信息删除"""
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '删除成功'}
    except Exception as err:
        context = {'info': '删除失败'}
        print(err)
    return render(request, 'myadmin/info.html', context)


def edit(request, uid=0):
    """加载信息编辑表单"""
    try:
        ob = User.objects.get(id=uid)
        context = {'user': ob}
        return render(request, 'myadmin/user/edit.html', context)
    except Exception as err:
        context = {'info': '没有找到要修改信息'}
        print(err)
        return render(request, 'myadmin/user/edit.html', context)


def update(request, uid):
    """执行信息修改"""
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '修改成功'}
    except Exception as err:
        context = {'info': '修改失败'}
        print(err)
    return render(request, 'myadmin/info.html', context)
