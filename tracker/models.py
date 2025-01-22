from django.db import models
from django.utils.timezone import now

# Create your models here.
class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=20)
    starting = models.BooleanField()
    dateTime = models.DateTimeField(default=now)


    def __str__(self):
        date = self.dateTime.strftime("%Y-%m-%d")
        time = self.dateTime.strftime("%H:%M:%S")
        return f"{self.activity} ({'Start' if self.starting else 'End'}) on {date} at {time}"