from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    teacher= models.CharField(max_length=250)
    credits=models.CharField(max_length=250)
    department=models.CharField(max_length=250)
    def __str__(self):
        return 'Teacher Name = '+ self.teacher + 'Department Name = '+ self.credits


class Student(models.Model):
    name= models.CharField(max_length=250)
    contact=models.CharField(max_length=250)
    courses=models.ForeignKey(Course,on_delete=models.CASCADE)

class Album(models.Model):
    name = models.CharField(max_length=250)
    singer = models.CharField(max_length=250)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

class Song(models.Model):
    name = models.CharField(max_length=250)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

class Appointments(models.Model):
    mentee = models.ForeignKey(User,on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, related_name='appointment_attendee',on_delete=models.SET_NULL, blank=True, null=True)
    startTime = models.BigIntegerField()
    endTime = models.BigIntegerField()
    status = models.IntegerField()
    channel = models.CharField(max_length=500)



