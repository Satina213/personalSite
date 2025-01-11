from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "newyear/index.html", {
        "year": now.year,
        "month": now.month,
        "day": now.day
    })