from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def AppHello(request,name = "Everyone"):
    return HttpResponse("Hello %s"%name)