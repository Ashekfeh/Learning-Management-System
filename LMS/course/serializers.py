from rest_framework import serializers

from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'duration', 'category_name')


# class TeacherSerializer(serializers.ModelSerializer):
#     course_name = serializers.CharField(source='course.title')

#     class Meta:
#         model = Teacher
#         fields = ('id','username', 'first_name', 'last_name', 'email', 'course_name')


# class StudentSerializer(serializers.ModelSerializer):
#     course_name = serializers.CharField(source='course.title')

#     class Meta:
#         model = Student
#         fields = ('id', 'username', 'firstname', 'lastname', 'email', 'course_name')


