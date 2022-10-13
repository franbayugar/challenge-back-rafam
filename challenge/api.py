from .models import Lesson, Course, User
from rest_framework import viewsets, permissions
from .serializers import LessonSerializer, CourseSerializer, UserSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LessonSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer