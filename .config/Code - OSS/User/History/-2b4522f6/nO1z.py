from django.shortcuts import render
from djang0.http import HttpResponse

def store(request):
    return HttpResponse("Hello")
