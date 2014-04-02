from django.db import models

from stage.models import Stage

class Salle(models.Model):
	num = models.CharField(max_length=5, primary_key=True)

	def __str__(self):
		return "%s" % (self.num)

class Soutenance(models.Model):
	idSoutenance = models.AutoField(primary_key=True)
	stage = models.ForeignKey(Stage, unique=True)
	datePassage = models.DateTimeField(verbose_name="Date de passage")
	dateFinPrevu = models.DateTimeField(verbose_name="Fin prévu")
	salle = models.ForeignKey(Salle, unique_for_date="datePassage")

	def __str__(self):
		return "%s" % (self.stage.intitule)

	def natural_key(self):
		return (self.idSoutenance, datePassage) + (self.stage.natural_key(),)