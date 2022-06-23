from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from homework.serailizers import CourseSerializer
# Create your views here.
from homework.models import HomeWork


class CourseAPIView(APIView):
    def get(self,request):
        course = HomeWork.objects.all()
        serializer = CourseSerializer(instance=course,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        serializer = CourseSerializer(instance=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

class CourseInfoAPIView(APIView):
    def get(self,request,pk):
        course = HomeWork.objects.get(pk=pk)
        serializer = CourseSerializer(instance=course)
        return Response(serializer.data,status.HTTP_200_OK)



