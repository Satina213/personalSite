from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def william(request):
    return HttpResponse("Hey Will!")

def david(request):
    return HttpResponse("Heyo, Dave")

def jessica(request):
    return HttpResponse("Yessica Jessica")

def bob(request):
    return HttpResponse("Yas Bob Yas!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })