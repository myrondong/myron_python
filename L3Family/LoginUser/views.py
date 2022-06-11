from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class RegList(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegSerializers

    def create(self, request, *args, **kwargs):
        res = RegSerializers(data=request.data)
        if res.is_valid():
            res.save()
            # res.errors 定义好的错误信息
        return Response(res.errors)


class LogList(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LogSerializers

    def create(self, request, *args, **kwargs):
        data = request.data
        res = LogSerializers(data=data)
        if res.is_valid():
            return Response(res.validated_data)
            # res.errors 定义好的错误信息
        return Response(res.errors)
