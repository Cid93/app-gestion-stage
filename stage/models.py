# -*- coding: utf-8 -*-
from django import forms
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
        return self.intitule+"-"+self.annee

    def natural_key(self):
        return {
            'intitule' : self.intitule
        }


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

    def natural_key(self):
        return {
            'nom' : self.nom,
            'prenom' : self.prenom,
            'telephone' : self.telephone}


class Etudiant(PersonneInterne):
    numEtu = models.IntegerField(primary_key=True)
    dateNaissance = models.DateField(verbose_name="Date de naissance")
    emailEtu = models.EmailField(max_length=80)
    adresse = models.CharField(max_length=100)
    cp = models.IntegerField(max_length=5)
    ville = models.CharField(max_length=50)
    promotion = models.ForeignKey(Promotion)
    class Meta:
        permissions = (
            ("rechercherconsulter_etudiant", "Peut rechercher et consulter les fiches d'étudiants"),
        )

    def search_result_header():
        html="<thead><tr><th>Promotion</th><th>Numéro</th><th>Nom</th><th>Prénom</th><th>E-mail</th></tr></thead>"
        return "%s" % (html)

    def search_result(self):
        html="<tr class=\"trLien\" onclick=\"document.location='/etudiant/"+str(self.numEtu)+"'\"><td>"+str(self.promotion)+"</td><td>"+str(self.numEtu)+"</td><td>"+self.nom+"</td><td>"+self.prenom+"</td><td>"+self.emailEtu+"</td></tr>"
        return "%s" % (html)

    def natural_key(self):
        return {'numEtu' : self.numEtu,
            'nom' : self.nom,
            'prenom' : self.prenom,
            'telephone' : self.telephone
            }




class Enseignant(PersonneInterne):
    idEnseignant = models.AutoField(primary_key=True)
    emailEns = models.EmailField(max_length=80)
    departement = models.CharField(max_length=80) # peut-être à séparer dans une classe département ?
    #numEns = models.IntegerField(primary_key=True)
    #grade = models.CharField(max_length=50)

    

    class Meta:
        permissions = (
            ("rechercherconsulter_enseignant", "Peut rechercher et consulter les fiches d'enseignants"),
        )

    def search_result_header():
        html="<thead><tr><th>Nom</th><th>Prénom</th><th>E-mail</th><th>Département</th></tr></thead>"
        return "%s" % (html)

    def search_result(self):
        html="<tr class=\"trLien\" onclick=\"document.location='/enseignant/"+str(self.idEnseignant)+"'\"><td>"+self.nom+"</td><td>"+self.prenom+"</td><td>"+self.emailEns+"</td><td>"+self.departement+"</td></tr>"
        return "%s" % (html)



class PersonneExterieure(Personne):
    idPersonneExt = models.AutoField(primary_key=True)
    emailPro = models.EmailField(max_length=80)
    entreprise=models.ForeignKey(Entreprise, related_name="personneExterieure_entreprise")

    def natural_key(self):
        return {
            'nom' : self.nom,
            'prenom' : self.prenom,
            'telephone' : self.telephone,
            'emailPro' : self.emailPro
        }



class Logiciel(models.Model):
    nomLog = models.CharField(primary_key=True, max_length=50)
    theme = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    class Meta:
        ordering = ('nomLog',)

    def __str__(self):
        return self.nomLog



class OffreStage(models.Model):
    intitule = models.CharField(max_length=100)
    sujet = models.CharField(max_length=512)
    # on stocke l'entreprise ici au cas où le tuteur de stage (personne ext) change d'entreprise
    entreprise = models.ForeignKey(Entreprise, related_name="stage_entreprise")
    nomLogiciels = models.ManyToManyField(Logiciel, null=True, blank=True)
    possibiliteEmbauche = models.NullBooleanField(null=True, default=None)
    valideOffreStage = models.NullBooleanField(default=False)
        #False : pas validé
        #True : validé
        #None : offre de stage prise par un étudiant

    class Meta:
        permissions = (
            ("valider_offrestage", "Peut valider une offre de stage"),
            ("postuler_offrestage", "Peut postuler à une offre de stage"),
        )

    def natural_key(self):
        return {
            'intitule' : self.intitule,
            'entreprise' : self.entreprise.natural_key(),
            }

    def __str__(self):
        return self.intitule

    def search_result_header():
        html="<thead><tr><th>Intitulé</th><th>Entreprise</th></tr></thead>"
        return "%s" % (html)

    def search_result(self):
        html="<tr><td>"+self.intitule+"</td><td>"+str(self.entreprise)+"</td></tr>"
        return "%s" % (html)

    def valider(self):
        setattr(self, 'valideOffreStage', True)
        self.save();
        return True

    def reserver(self):
        setattr(self, 'valideOffreStage', None)
        self.save();
        return True



class Stage(OffreStage):
    idStage = models.AutoField(primary_key=True)
    etudiant = models.ForeignKey(Etudiant, related_name="stage_etudiant")
    dateDebut = models.DateField()
    dateFin = models.DateField()
    persConvention = models.ForeignKey(PersonneExterieure, related_name="stage_persConvention")
    maitreStage = models.ForeignKey(PersonneExterieure, related_name="stage_maitreStage")
    enseignantTuteur = models.ForeignKey(Enseignant, related_name="stage_enseignantTuteur")
    valideStage = models.BooleanField(default=False) 
    # Un étudiant peut changer de promotion donc on préfère stocker la promotion dans le stage
    # promotion = models.ForeignKey(Promotion)


    class Meta:
        ordering = ('intitule',)
        permissions = (
            ("valider_stage", "Peut valider un stage"),
            ("genererdocuments_stage", "Peut générer les documents propres à un stage (convention)"),
            ("noter_stage", "Peut noter un stage"),
        )

    def __str__(self):
        return self.intitule

    def natural_key(self):
        return {
            'id' : self.idStage,
            'intitule' : self.intitule,
            'sujet' : self.sujet,
            'dateDeDebut' : self.dateDebut,
            'dateDeFin' : self.dateFin,
            'etudiant' : self.etudiant.natural_key(),
            'maitreStage' : self.maitreStage.natural_key(),
            'enseignantTuteur' : self.enseignantTuteur.natural_key()
        }

    def search_result_header():
        html="<thead><tr><th>Intitulé</th><th>Etudiant</th><th>Enseignant Tuteur</th><th>Entreprise</th></tr></thead>"
        return "%s" % (html)

    def search_result(self):
        idEnt = Entreprise.objects.get(nom=str(self.entreprise)).idEntreprise
        html='<tr><td><a href="/stage/'+str(self.idStage)+'">'+self.intitule+'</td><td>'+str(self.etudiant)+'</td><td>'+str(self.enseignantTuteur)+'</td><td><a href="/entreprise/'+str(idEnt)+'">'+str(self.entreprise)+'</a></td></tr>'
        return "%s" % (html)



class EnseignantResp(models.Model):
    enseignant = models.ForeignKey(Stage,related_name="EnseignantResp_enseignant")
    stage = models.ManyToManyField(Stage)
    priorite_reservation = models.IntegerField(max_length=2)
    validation_resp=models.BooleanField(default=False)