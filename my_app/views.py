# views.py

from django.shortcuts import render
from django.http import HttpResponse

def page1(request):
    return HttpResponse("This is page 1")

def page2(request):
    return HttpResponse("This is page 2")

def page3(request):
    return HttpResponse("This is page 3")

def page4(request):
    return HttpResponse("This is page 4")

def page5(request):
    return HttpResponse("This is page 5")
