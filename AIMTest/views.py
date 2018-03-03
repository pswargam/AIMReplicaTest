
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from .models import Appointments




def redirectToCalendar(request):
    return render(request,"calendar.html")

def getValuesForCalendar(request):

    calendarSet=Appointments.objects.all()
    calendarData=serializers.serialize('json',calendarSet,fields=('attendee','startTime','endTime'),use_natural_foreign_keys=True, use_natural_primary_keys=True)
    #return JsonResponse(calendarData, safe=False)
    return HttpResponse(calendarData, content_type='application/json')