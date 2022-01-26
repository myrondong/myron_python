from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def add_publish(request):
    if request.method == 'POST':
        # 获取表达内容
        publisher_name = request.POST.get('name')
        publisher_address = request.POST.get('address')
        print(publisher_name)
        # 保存数据库
        models.Publisher.objects.create(name=publisher_name, address=publisher_address)
        # 重定向
        return redirect('/app01/publish_list')
    return render(request, 'add_publisher.html')


def publish_list(request):
    return render(request, 'publisher_list.html')
