from django.db import models
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.
class Onpollclub(models.Model):
    admin= models.CharField(max_length=25)
    club_name = models.CharField(max_length=200,)
    club_info = models.TextField(max_length=20000)
    club_logo = models.ImageField(upload_to='media_/club_logo', )
    release_date = models.TimeField(default=datetime.now())
