from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Market(models.Model):


	image=models.ImageField( default = 'img/img.jpg')
	
	message=models.CharField(max_length=500)
	

	

	class Meta:
		verbose_name_plural = "market"

	def __str__(self):
		return self.message

