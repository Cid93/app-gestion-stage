# -*- coding: utf-8 -*-

#from django.core.management import setup_environ
#from gestionStage import settings
#setup_environ(settings)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestionStage.settings")
from django.forms import ModelForm
from entreprise.models import Entreprise
from stage.models import Personne, PersonneExterieure, Diplome, Promotion, Etudiant, Enseignant, Stage
from pprint import pprint

import json

entreprise = json.load(open("entreprise.json")) 	#encoding='utf-8'
stage = json.load(open("stage.json")) 				#encoding='utf-8'
enseignants = json.load(open("enseignants.json")) 	#encoding='utf-8'
etudiants = json.load(open("etudiants.json")) 		#encoding='utf-8'
personnesExt = json.load(open("personnes_exterieures.json")) #encoding='utf-8'
promotions = json.load(open("promotions.json")) #encoding='utf-8'
diplomes = json.load(open("diplomes.json")) #encoding='utf-8'


for e in entreprise:
	Entreprise(
		idEntreprise=e["idEntreprise"],
		nom=e["nom"],
		adresse=e["adresse"],
		codePostal=e["codePostal"],
		ville=e["ville"],
		pays=e["pays"],
		telephone=e["telephone"],
		fax=e["fax"]
	).save()

for e in enseignants:
	Enseignant(
		idEnseignant=e["idEnseignant"],
		nom=e["nom"],
		prenom=e["prenom"],
		emailPerso=e["emailPerso"],
		civilite=e["civilite"],
		telephone=e["telephone"],
		emailEns=e["emailEns"],
		departement=e["departement"]
	).save()

for e in etudiants:
	Etudiant(
		numEtu=e["numEtu"], #PRIMARY KEY
		nom=e["nom"],
		prenom=e["prenom"],
		emailPerso=e["emailPerso"],
		civilite=e["civilite"],
		telephone=e["telephone"],
		dateNaissance=e["dateNaissance"],
		emailEtu=e["emailEtu"],
		adresse= e["adresse"],
		cp=e["cp"],
		ville=e["ville"]
	).save()

for p in personnesExt:
	PersonneExterieure(
		idPersonneExt=p["idPersonneExt"],
		nom=p["nom"],
		prenom=p["prenom"],
		emailPerso=p["emailPerso"],
		civilite=p["civilite"],
		telephone=p["telephone"],
		emailPro=p["emailPro"],
		entreprise=Entreprise.objects.get(pk=p["entreprise"])
	).save()


for d in diplomes:
	diplome=Diplome(
		nom=d["nom"],
		specialite=d["specialite"]
	)
	diplome.save()


for p in promotions:
	promo=Promotion(
		diplome=Diplome.objects.get(pk=p["diplome"]),
		intitule=p["intitule"],
		annee=p["annee"]
	)
	promo.save()

for s in stage:	
	internship=Stage(
		etudiant=Etudiant.objects.get(pk=s["etudiant"]),
		intitule=s["intitule"],
		sujet=s["sujet"],
		dateDebut=s["dateDebut"],
		dateFin=s["dateFin"],
		entreprise=Entreprise.objects.get(pk=s["entreprise"]),
		persConvention=PersonneExterieure.objects.get(pk=s["persConvention"]),
		maitreStage=PersonneExterieure.objects.get(pk=s["maitreStage"]),
		enseignantTuteur=Enseignant.objects.get(pk=s["enseignantTuteur"]),
		promotion=Promotion.objects.get(pk=s["promotion"])
	)
	internship.save()



# #charger les permissions
# from django.contrib.auth.models import Permission, User, Group
# from django.contrib.contenttypes.models import ContentType

# personne_content_type = ContentType.objects.get_for_model(Personne)
# perms= json.load(open("permissions.json"))
# PERMS = {}

# for p in perms:
# 	perm=Permission.objects.create(
# 		codename=p["codename"],
# 		name=p["name"],
# 		content_type=personne_content_type
# 	)
# 	perm.save()
# 	PERMS[p["codename"]] = perm


# #charger les groupes
# groups=json.load(open("groups.json"))
# GROUPS={}
# for g in groups:
# 	group=Group.objects.create(name=g["name"])
# 	group.save()
# 	for p in g["permissions"]:
# 		group.permissions.add(PERMS[p])
# 	group.save()
# 	GROUPS[g["name"]]=group


# #charger les utilisateurs
# users=json.load(open("users.json"))
# USERS={}
# for u in users:
# 	user=User.objects.create_user(
# 		username=u["username"],
# 		password=u["password"],
# 		first_name=u["first_name"],
# 		last_name=u["last_name"],
# 		email=u["email"]
# 	)
# 	user.save()

# 	for g in u["groups"]:
# 		user.groups.add(GROUPS[g])
# 	user.save()
# 	USERS[u["username"]]=user


