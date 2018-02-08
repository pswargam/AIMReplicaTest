from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from .models import Course,Student,Song


def index(request):
    return HttpResponse("<h1> This is a first django response</h1>")


def mainpage(request):
    c={}
    return render(request,"index.html")

def authorize(request):
    username=request.POST.get("user")
    password=request.POST.get("password")

    user=authenticate(username=username, password=password)
    if user is not None:
        songsSet=Song.objects.filter(owner=user)
        print(songsSet.__len__())
        return render(request, "dashboard.html", {'setOfSongs': songsSet,'user':user})
    else:
        return HttpResponse("<h1> Incorrect username</h1>")