from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(resquest):
    return HttpResponse('Hi I LOVE U')

def propose(request):
    return HttpResponse('<marquee>yes i love you</marquee>')
