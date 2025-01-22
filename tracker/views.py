from django.shortcuts import render
from .models import Log
from datetime import datetime
import pytz

3
# Create your views here.
def index(request):
    return render(request, "tracker/index.html")

def view_logs(request):
    # Fetch all logs from the database
    logs = Log.objects.all().order_by('-dateTime') #Order by date and time (most recent first)
   # Define the timezone (e.g., Central Time)
    timezone = pytz.timezone("America/Chicago")  # Adjust based on your timezone
    now_aware = datetime.now(timezone)  # Make timezone-aware datetime

    # Format the date and time with the UTC offset
    today = now_aware.strftime("%Y-%m-%d")  # Format for date input
    now = now_aware.strftime("%H:%M")  # Time with UTC offset, e.g., "14:30-0600"

    #Pass logs to template
    context = {
        'logs': logs,
        'today': today,
        'now': now,
    }
    return render(request, 'tracker/log.html', context)


