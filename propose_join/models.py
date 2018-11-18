from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from dateutil.relativedelta import relativedelta
from registration.models import Profile

class ProposedClub(models.Model):
    name=models.ForeignKey(User,on_delete=models.PROTECT)
    club_name=models.CharField(max_length=200,unique=True)
    club_info =models.TextField(max_length=20000)
    club_logo=models.ImageField(upload_to='media_/club_logo',)

    def __str__(self):
        return  str(self.club_name) + " by " + str(self.name)



class ExistingClub(models.Model):
    club_name  = models.CharField(max_length=200,unique=True)
    admin = models.ManyToManyField(User)
    club_info  =models.TextField(max_length=20000)
    club_logo = models.ImageField(upload_to='media_/club_logo', blank=True)

    def __str__(self):
        return str(self.club_name) + " admin--> " + str(self.admin)



class ClubMember(models.Model):
    user_name = models.OneToOneField(User,on_delete=models.PROTECT)
    clubs_joined = models.ManyToManyField(ExistingClub)

    def __str__(self):
        return str(self.user_name)