from django.db import models

# Create your models here.
class Courses(models.Model):
    teacher= models.CharField(max_length=250);
    credits=models.CharField(max_length=250);
    department=models.CharField(max_length=250);
    def __str__(self):
        return 'Teacher Name = '+ self.teacher + 'Department Name = '+ self.credits


class Students(models.Model):
    name= models.CharField(max_length=250);
    contact=models.CharField(max_length=250);
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE);
