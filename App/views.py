from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def AppHello(request,name = "Everyone"):
    return HttpResponse("Hello %s"%name)

def AddTask(request,task):
    NewTask = Todo.objects.create(name = task)
    NewTask.save()
    return HttpResponse("Task %s saved"%task)