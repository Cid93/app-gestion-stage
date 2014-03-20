# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from entreprise.models import Entreprise
# Create your models here..


class Diplome(models.Model):
    idDiplome = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    specialite = models.CharField(max_length=80)

    class Meta:
        ordering = ('nom',)

    def __str__(self):
        return self.nom

class Promotion(models.Model):
    idPromotion = models.AutoField(primary_key=True)
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

class PersonneInterne(Personne):
    username=models.ForeignKey(User, related_name="personneInterne_username")

class Etudiant(PersonneInterne):
    numEtu = models.IntegerField(primary_key=True)
    dateNaissance = models.DateField(verbose_name="Date de naissance")
    emailEtu = models.EmailField(max_length=80)
    adresse = models.CharField(max_length=100)
    cp = models.IntegerField(max_length=5)
    ville = models.CharField(max_length=50)

class Enseignant(PersonneInterne):
    idEnseignant = models.AutoField(primary_key=True)
    emailEns = models.EmailField(max_length=80)
    departement = models.CharField(max_length=80) # peut-être à séparer dans une classe département ?
    #numEns = models.IntegerField(primary_key=True)
    #grade = models.CharField(max_length=50)

class PersonneExterieure(Personne):
    idPersonneExt = models.AutoField(primary_key=True)
    emailPro = models.EmailField(max_length=80)
    entreprise=models.ForeignKey(Entreprise, related_name="personneExterieure_entreprise")

class Logiciel(models.Model):
    nomLog = models.CharField(primary_key=True, max_length=50)
    theme = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    class Meta:
        ordering = ('nomLog',)

    def __str__(self):
        return self.nomLog

class Stage(models.Model):
    idStage = models.AutoField(primary_key=True)
    etudiant=models.ForeignKey(Etudiant, related_name="stage_etudiant")
    intitule=models.CharField(max_length=100)
    sujet = models.CharField(max_length=512)
    dateDebut=models.DateTimeField()
    dateFin=models.DateTimeField()
    # on stocke l'entreprise ici au cas où le tuteur de stage (personne ext) change d'entreprise
    entreprise=models.ForeignKey(Entreprise, related_name="stage_entreprise")
    persConvention=models.ForeignKey(PersonneExterieure, related_name="stage_persConvention")
    maitreStage=models.ForeignKey(PersonneExterieure, related_name="stage_maitreStage")
    enseignantTuteur=models.ForeignKey(Enseignant, related_name="stage_enseignantTuteur")
    # Un étudiant peut changer de promotion donc on préfère stocker la promotion dans le stage
    promotion = models.ForeignKey(Promotion)
    nomLogiciels = models.ManyToManyField(Logiciel, null=True, blank=True)

    class Meta:
        ordering = ('intitule',)

    def __str__(self):
        return self.intitule

class EnseignantResp(models.Model):
    enseignant = models.ForeignKey(Stage,related_name="EnseignantResp_enseignant")
    stage = models.ManyToManyField(Stage)
    priorite_reservation = models.IntegerField(max_length=2)
    validation_resp=models.BooleanField(default=False)




