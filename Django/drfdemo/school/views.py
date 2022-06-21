
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from school.models import Student
from school.serailizers import StudentModelSerializer
from rest_framework.response import Response

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

