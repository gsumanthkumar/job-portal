from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class postjob(models.Model):
    jobposter = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50,default=None)
    jobname = models.CharField(max_length=100)
    companyname = models.CharField(max_length=50)
    package = models.IntegerField()
    description = models.CharField(max_length=250,default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.companyname

