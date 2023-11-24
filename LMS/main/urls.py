from django.urls import include, path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()


router.register(r'courses', CourseViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'students', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]