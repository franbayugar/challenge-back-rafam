from unicodedata import name
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    name = models.CharField(max_length = 200)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name= models.CharField(max_length = 200)
    lessons = models.ManyToManyField(Lesson)
    users = models.ManyToManyField('self')
    
    def __str__(self):
        return self.name