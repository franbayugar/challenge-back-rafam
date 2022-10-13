from rest_framework import serializers
from .models import Lesson, Course, User

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'url', 'name', 'course')
    
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'name', 'lessons', 'users')
        
class UserLessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name','lessons')
        
class UserFriendsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name','users')