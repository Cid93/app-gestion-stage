from django.db import models
#from django.contrib.auth.models import User
#from stage.models import PersonneExterieure
# Create your models here.

class Entreprise(models.Model):
	idEntreprise = models.AutoField(primary_key=True)
	nom=models.CharField(max_length=100)
	adresse=models.CharField(max_length=250)
	codePostal=models.BigIntegerField(max_length=10)
	ville=models.CharField(max_length=50)
	pays=models.CharField(max_length=30)
	telephone=models.BigIntegerField(max_length=22)
	fax=models.BigIntegerField(max_length=14, blank=True, null=True)

	class Meta:
		permissions = (
			("valider_entreprise", "Peut valider une entreprise"),
		)

	def __str__(self):
		return "%s" % (self.nom)

	def natural_key(self):
		return { 'idEntreprise' : self.idEntreprise,
			'nom' : self.nom}
	
	def search_result_header():
		html="<thead><tr><th>Nom</th><th>Adresse</th><th>Ville</th><th>Téléphone</th></tr></thead>"
		return "%s" % (html)

	def search_result(self):
		html='<tr><td><a href="/entreprise/'+str(self.idEntreprise)+'">'+self.nom+'</a></td><td>'+self.adresse+'</td><td>'+self.ville+'</td><td>'+str(self.telephone)+'</td></tr>'
		return "%s" % (html)