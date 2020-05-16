from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Chart(models.Model):


    countries=models.CharField(max_length=500)
    
    numbers=models.IntegerField()
    

    

    class Meta:
        verbose_name_plural = "Chart"

    def __str__(self):
        return self.countries



class DataProcess(models.Model):
    email = models.EmailField()
    file = models.FileField(upload_to='media/')
    body = models.TextField()
    author = models.ForeignKey(User, default=None,on_delete=models.SET_DEFAULT)
    

    class Meta:
        verbose_name_plural = "DataProcess"

    def __str__(self):
        return self.email







class Post(models.Model):
    title=models.FileField(upload_to='media/')
    content= models.TextField()



class MessageUs(models.Model):
    email1= models.EmailField()
    yMessage= models.TextField()
    date = models.DateTimeField("date sent", default=datetime.now())