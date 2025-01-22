from django.shortcuts import render
from .models import Log

# Create your views here.
def index(request):
    return render(request, "tracker/index.html")

def view_logs(request):
    # Fetch all logs from the database
    logs = Log.objects.all().order_by('-dateTime') #Order by date and time (most recent first)
    #Pass logs to template
    context = {
        'logs': logs,
    }
    return render(request, 'tracker/log.html', context)


