from .models import Lesson, Course, User
from rest_framework import viewsets, permissions, filters
from .serializers import LessonSerializer, CourseSerializer, UserSerializer, UserLessonSerializer, UserFriendsSerializer

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
    

class UserLessonsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLessonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
    
class UserFriendsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserFriendsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )