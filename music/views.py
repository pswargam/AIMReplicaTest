from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1> This is a first django response</h1>")


def mainpage(request):
    c={}
    return render(request,"index.html")
