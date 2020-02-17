from django.db import models

# Using inbuilt 'User' module
from django.contrib.auth.models import User 

# models starts from here
# creating Main model as 'Subject', sub model as 'Courses' and 
# sub model for course as 'Module'.

# Main Module 'Subject' 

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

# 'Course' sub model for 'Subject'
class Course(models.Model):
    owner = models.ForeignKey(User, related_name='course_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

# 'Module' sub model for 'Course'
class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title