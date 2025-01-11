from django.shortcuts import render
from django.http import HttpResponse

tasks = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })