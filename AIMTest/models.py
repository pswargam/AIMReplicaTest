from django.db import models
from django.contrib.auth.models import User

#AIM Models

class Appointments(models.Model):
    mentee = models.ForeignKey(User,on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, related_name='appointment_attendee',on_delete=models.SET_NULL, blank=True, null=True)
    startTime = models.BigIntegerField()
    endTime = models.BigIntegerField()
    status = models.IntegerField()
    channel = models.CharField(max_length=500)



