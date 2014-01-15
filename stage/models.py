# -*- coding: utf-8 -*-

from django.db import models
#from django.contrib.auth.models import User
from entreprise.models import Entreprise
# Create your models here..


class Diplome(models.Model):
    nom = models.CharField(max_length=20)
    specialite = models.CharField(max_length=80)

    class Meta:
        ordering = ('nom',)

    def __str__(self):
        return self.nom

class Promotion(models.Model):
    intitule = models.CharField(max_length=20)
    annee = models.CharField(max_length=10)
    diplome = models.ForeignKey(Diplome)

    class Meta:
        ordering = ('intitule',)

    def __str__(self):
        return self.intitule

class Personne(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    emailPerso = models.EmailField(max_length=80)
    typeCivilite = (('M.', 'Monsieur'),('Mme', 'Madame'),('Mlle', 'Mademoiselle'))
    civilite = models.CharField(max_length=15,choices=typeCivilite,default='M.')
    telephone = models.CharField(max_length=14, null=True, blank=True)
    
    class Meta:
        ordering = ('nom',)

    def __str__(self):
        return self.prenom +" "+ self.nom

class Etudiant(Personne):
    promo = models.ForeignKey(Promotion)
    numEtud = models.IntegerField(primary_key=True)
    dateNaissance = models.DateField(verbose_name="Date de naissance")
    emailEtu = models.EmailField(max_length=80)
    adresse = models.CharField(max_length=100)
    cp = models.IntegerField(max_length=5)
    ville = models.CharField(max_length=50)


class Enseignant(Personne):
    emailEns = models.EmailField(max_length=80)
    departement = models.CharField(max_length=80)
    #numEns = models.IntegerField(primary_key=True)
    #grade = models.CharField(max_length=50)


class Stage(models.Model):
    etudiant=models.ForeignKey(Etudiant, related_name="etudiant")
    intitule=models.CharField(max_length=100)
    sujet = models.CharField(max_length=512)
    dateDebut=models.DateTimeField(null=True, blank=True)
    dateFin=models.DateTimeField(null=True, blank=True)
    entreprise=models.ForeignKey(Entreprise, related_name="entreprise")

    class Meta:
        ordering = ('intitule',)

    def __str__(self):
        return self.intitule

class logiciel(models.Model):
    nomLog = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)

class Stage_logiciel(models.Model):
    stage = models.ForeignKey(Stage)
    nomLogiciel=models.ManyToManyField(logiciel)





class EnseignantResp(Enseignant):        
    stage = models.ManyToManyField(Stage)
    priorite_reservation= models.IntegerField(max_length=2)
    validation_resp=models.IntegerField(max_length=1)