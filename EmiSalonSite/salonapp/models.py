from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    est_time = models.DurationField() # uses datetime.timedelta(hours=x, minutes=y) if init with code
    
    
    