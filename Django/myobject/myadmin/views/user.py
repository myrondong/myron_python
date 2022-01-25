# 员工视图文件
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import hashlib


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
    return render(request, 'myadmin/index/index.html')


def insert(request):
    """执行信息添加"""
    try:
        ob = User()
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
    return render(request, 'myadmin/info。html', context)


def delete(request):
    """执行信息删除"""
    return render(request, 'myadmin/index/index.html')


def edit(request):
    """加载信息编辑表单"""
    return render(request, 'myadmin/index/index.html')


def update(request):
    """执行信息修改"""
    return render(request, 'myadmin/index/index.html')
