from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class LCstudent(ListCreateAPIView):
     queryset=Student.objects.all()
     serializer_class=StudentSerializer

class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    


