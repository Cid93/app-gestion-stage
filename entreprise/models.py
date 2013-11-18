from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entreprise(models.Model):
	nom=models.CharField(max_length=100)
	adresse=models.CharField(max_length=250)
	codePostal=models.BigIntegerField(max_length=10)
	ville=models.CharField(max_length=50)
	pays=models.CharField(max_length=30)
	telephone=models.BigIntegerField(max_length=22)
	fax=models.BigIntegerField(max_length=14)

	def __str__(self):
		return "%s" % (self.nom)


