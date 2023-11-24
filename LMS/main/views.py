from rest_framework import viewsets

from .serializers import *
from .models import *


class CourseViewSet(viewsets.ModelViewSet):
    
    queryset = Course.objects.all()

    serializer_class = CourseSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer