from  rest_framework.viewsets import ModelViewSet
from stuapi.models import Student
from .serailizers import StudentModelSerializers
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers