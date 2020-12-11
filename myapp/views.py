from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to prac1 app</h1>")

def base(request):
    return render(request,"myapp/base.html",{"name":"chandu","age":23})

def name(request):
    return render(request,"myapp/name.html",{"name":"mouli","age":23})

def wel(request):
    return render(request,"myapp/wel.html")
