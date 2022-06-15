from django.views import View
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response # drf Response 是HttpResponse的子类
# Create your views here.

class StudentDjView(View):
    """
    Dj 下的view
    """
    def get(self,request):# Dj 提供视图的View，在视图中的request变量是WSGIRequest
        print(f"request={request}") # <WSGIRequest:->父类 -》django.http.response.HttpResponse
        return HttpResponse('OK')



class StudentAPIView(APIView):
    """
    rest_framework 下面的View
    """

    def get(self,request):
        print(f"drf request={request}") # request=<rest_framework.request.Request: GET '/reqs/students/'>
        # 是属于drf单独申请的请求处理对象，与django提供的HttpRequest不是同一个对象
        print(f"dj request={request._request}") # 这个属于dj的，<WSGIRequest:->父类 -》django.http.response.HttpResponse
        return Response({"msg":"OK"})

    def post(self,request):
        # 添加数据
        """获取请求体数据"""
        # request.data={'a': '1212', 'b': 'ccccc'}
        print(f"request.data={request.data}") # 接受数据已经被parser解析器自动解析成为字典对象
        # 提取数据
        print(f"{request.data.get('name')}")
        """获取查询参数/查询字符串"""
        # 获取地址栏上面的参数

        # http://127.0.0.1:8000/up/users/?action=login 例如获取action 后面参数
        # request.query_params == dj的 reques.GET
        print(f"{request.query_params}")
        return Response({"msg": "OK"})

    def put(self,request):
        # 更新数据
        return Response({"msg":"OK"})

    def patch(self,request):
        # 更新部分数据
        return Response({"msg":"OK"})

    def delete(self,request):
        # 删除操作
        return Response({"msg":"OK"})