from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banks(models.Model):
	ifsc = models.CharField(max_length=20)
	bank_id = models.IntegerField()
	branch = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	bank_name = models.CharField(max_length=255)
	

	def __str__(self):
		return "{} - {}".format(self.bank_name, self.city)



