# -*- coding: utf-8 -*-

#from django.core.management import setup_environ
#from gestionStage import settings
#setup_environ(settings)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestionStage.settings")
from django.forms import ModelForm
from entreprise.models import Entreprise
from stage.models import Personne,Diplome,Promotion,Etudiant,Stage
from pprint import pprint

import json

entreprise = json.load(open("entreprise.json")) #encoding='utf-8'
#pprint(entreprise)
stage = json.load(open("stage.json")) #encoding='utf-8'


for e in entreprise:
	contact= Personne(nom=e["contact"]["nom"],prenom=e["contact"]["prenom"],emailPerso=e["contact"]["emailPerso"],civilite=e["contact"]["civilite"],telephone=e["contact"]["telephone"])
	contact.save()
	persConvention= Personne(nom=e["persConvention"]["nom"],prenom=e["persConvention"]["prenom"],emailPerso=e["persConvention"]["emailPerso"],civilite=e["persConvention"]["civilite"],telephone=e["persConvention"]["telephone"])
	persConvention.save()
	maitreStage= Personne(nom=e["maitreStage"]["nom"],prenom=e["maitreStage"]["prenom"],emailPerso=e["maitreStage"]["emailPerso"],civilite=e["maitreStage"]["civilite"],telephone=e["maitreStage"]["telephone"])
	maitreStage.save()
	company = Entreprise(nom=e["nom"],adresse=e["adresse"],codePostal=e["codePostal"],ville=e["ville"],pays=e["pays"],telephone=e["telephone"],fax=e["fax"],contact=contact,persConvention=persConvention,maitreStage=maitreStage)
	#company.contact=contact
	#company.persConvention=persConvention
	#company.maitreStage=maitreStage
	company.save()

for s in stage:
	diplome=Diplome(nom=s["etudiant"]["promo"]["diplome"]["nom"],specialite=s["etudiant"]["promo"]["diplome"]["specialite"])
	diplome.save()
	promo=Promotion(diplome=diplome,intitule=s["etudiant"]["promo"]["intitule"],annee=s["etudiant"]["promo"]["annee"])
	promo.save()
	personne=Personne(nom=s["etudiant"]["nom"],prenom=s["etudiant"]["prenom"],emailPerso=s["etudiant"]["emailPerso"],civilite=s["etudiant"]["civilite"],telephone=s["etudiant"]["telephone"])
	personne.save()
	etudiant=Etudiant(promo=promo,nom=personne.nom,prenom=personne.prenom,emailPerso=personne.emailPerso,civilite=personne.civilite,telephone=personne.telephone,numEtud=s["etudiant"]["numEtud"],dateNaissance=s["etudiant"]["dateNaissance"],emailEtu=s["etudiant"]["emailEtu"],adresse=s["etudiant"]["adresse"],cp=s["etudiant"]["cp"],ville=s["etudiant"]["ville"])
	etudiant.save()
	internship=Stage(etudiant=etudiant,intitule=s["intitule"],sujet=s["sujet"],dateDebut=s["dateDebut"],dateFin=s["dateFin"],entreprise=company)
	internship.save()



#charger les permissions
from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType

personne_content_type = ContentType.objects.get_for_model(Personne)
perms= json.load(open("permissions.json"))
PERMS = {}

for p in perms:
	perm=Permission.objects.create(
		codename=p["codename"],
		name=p["name"],
		content_type=personne_content_type
	)
	perm.save()
	PERMS[p["codename"]] = perm


#charger les groupes
groups=json.load(open("groups.json"))
GROUPS={}
for g in groups:
	group=Group.objects.create(name=g["name"])
	group.save()
	for p in g["permissions"]:
		group.permissions.add(PERMS[p])
	group.save()
	GROUPS[g["name"]]=group


#charger les utilisateurs
users=json.load(open("users.json"))
USERS={}
for u in users:
	user=User.objects.create_user(
		username=u["username"],
		password=u["password"],
		first_name=u["first_name"],
		last_name=u["last_name"],
		email=u["email"]
	)
	user.save()

	for g in u["groups"]:
		user.groups.add(GROUPS[g])
	user.save()
	USERS[u["username"]]=user


