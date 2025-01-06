from django.db import models
import os
from datetime import datetime
# Create your models here.


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploadd/',filename)

class Eventdatapaper(models.Model):
    Name = models.CharField(max_length=25,default="")
    Roll_no = models.CharField(max_length=50,default="")
    Email = models.CharField(max_length=50,default="")
    Event_name = models.CharField(max_length=255,default="")
    Event_cordinator = models.CharField(max_length=100,default="")
    Event_date = models.DateField(auto_now_add=True)
    Latitude = models.FloatField(default=0,null=True)
    Longitude = models.FloatField(default=0,null=True)
    Time = models.CharField(max_length=20, default="",null=True)
    Date = models.DateField(auto_now_add=True,null=True)
    Place = models.CharField(max_length=30,default="",null=True)
    District = models.CharField(max_length=30,default="",null=True)
    Image = models.FileField(upload_to=filepath, null=True, blank=True)


class Eventdataproject(models.Model):
    Name = models.CharField(max_length=25,default="")
    Roll_no = models.CharField(max_length=50,default="")
    Email = models.CharField(max_length=50,default="")
    Event_name = models.CharField(max_length=255,default="")
    Event_cordinator = models.CharField(max_length=100,default="")
    Event_date = models.DateField(default="")
    Latitude = models.FloatField(default=0,null=True)
    Longitude = models.FloatField(default=0,null=True)
    Time = models.CharField(max_length=20, default="",null=True)
    Date = models.DateField(auto_now_add=True,null=True)
    Place = models.CharField(max_length=30,default="",null=True)
    District = models.CharField(max_length=30,default="",null=True)
    Image = models.FileField(upload_to=filepath, null=True, blank=True)

class Eventdatatechnical(models.Model):
    Name = models.CharField(max_length=25,default="")
    Roll_no = models.CharField(max_length=50,default="")
    Email = models.CharField(max_length=50,default="")
    Event_name = models.CharField(max_length=255,default="")
    Event_cordinator = models.CharField(max_length=100,default="")
    Event_date = models.DateField(default="")
    Latitude = models.FloatField(default=0,null=True)
    Longitude = models.FloatField(default=0,null=True)
    Time = models.CharField(max_length=20, default="",null=True)
    Date = models.DateField(auto_now_add=True,null=True)
    Place = models.CharField(max_length=30,default="",null=True)
    District = models.CharField(max_length=30,default="",null=True)
    Image = models.FileField(upload_to=filepath, null=True, blank=True)


# class finalpaper(models.Model):
#     Name = models.CharField(max_length=25,default="")
#     Roll_no = models.CharField(max_length=50,default="")
#     Email = models.CharField(max_length=50,default="")
#     Event_name = models.CharField(max_length=255,default="")
#     Event_cordinator = models.CharField(max_length=100,default="")
#     Event_date = models.DateField(auto_now_add=True)
#     Latitude = models.FloatField(default=0,null=True)
#     Longitude = models.FloatField(default=0,null=True)
#     Time = models.CharField(max_length=20, default="",null=True)
#     Date = models.DateField(auto_now_add=True,null=True)
#     Place = models.CharField(max_length=30,default="",null=True)
#     District = models.CharField(max_length=30,default="",null=True)
#     Image = models.FileField(upload_to=filepath, null=True, blank=True)

