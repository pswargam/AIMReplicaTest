from django.contrib.auth import authenticate
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from re import sub
from .models import Song, Album, User,Appointments
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

def mainpage(request):
    c={}
    return render(request,"index.html")

def authorize(request):
    username=request.POST.get("user")
    password=request.POST.get("password")

    user=authenticate(username=username, password=password)
    if user is not None:
        albumSet=Album.objects.filter(owner=user)

        return render(request, "dashboard.html", {'setOfAlbums': albumSet,'user':user,'userid':user.pk})
    else:
        return HttpResponse("<h1> Incorrect username</h1>")

def redirectToAllSongs(request):
    userId= request.POST.get("primaryUser")

    userr = User.objects.filter(pk=userId)


    songsSet=Song.objects.filter(owner=userr[0])
    songsData=serializers.serialize('json',songsSet,fields=('name','owner'))
    #print(songsData)
    return JsonResponse(songsData,safe=False)

def redirectToCalendar(request):
    return render(request,"calendar.html")

def getValuesForCalendar(request):

    calendarSet=Appointments.objects.all()
    calendarData=serializers.serialize('json',calendarSet,fields=('attendee','startTime','endTime'),use_natural_foreign_keys=True, use_natural_primary_keys=True)
    #return JsonResponse(calendarData, safe=False)
    return HttpResponse(calendarData, content_type='application/json')