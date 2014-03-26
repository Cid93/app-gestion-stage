from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.template import RequestContext
from django.core import serializers

from datetime import datetime

from gestionStage.shortcuts import render
from stage.models import Stage, Etudiant, Enseignant, PersonneExterieure
from planning.models import Soutenance
from planning.forms import SoutenanceSelection, SoutenanceForm, SalleForm

import json

def show_planning(request):
	tableDHeure = range(13)
	tableDHeureHEt1 = range(13)
	for chiffre in tableDHeure:
		chiffre = chiffre + 7
	for chiffre in tableDHeureHEt1:
		chiffre = chiffre + 8

	return render(
		request,
		"planning/planning.html",
		{'form' : SoutenanceSelection,
		'taille' : tableDHeure,
		'TEtUn' : tableDHeureHEt1}
	)

def show_soutenance(request, pk):
	return render(
		request,
		"planning/soutenance.html",
		{'soutenance' : Soutenance.objects.get(idSoutenance=pk)})

def addSoutenance(request):
	if request.method == 'POST':  				# Si une requête POST a été passée
		form = SoutenanceForm(request.POST)  	# On récupère les données
		
		if form.is_valid(): 					# Si les données reçues sont valides
			form.save()
			return HttpResponseRedirect('/planning/')
		else:									# Si les données reçues sont invalides
			con = { 'actionAFaire' : 'Ajouter', 'form' : form}
			return render(request,'planning/forms.html', con)

	else: 										# Pas de requête POST
		form = SoutenanceForm()  				# On crée un formulaire vide
		con = { 'actionAFaire' : 'Ajouter', 'form' : form}
		return render(request,'planning/forms.html', con)


def addSalle(request):
	if request.method == 'POST':  				# S'il s'agit d'une requête POST
		form = SalleForm(request.POST)  	# Nous reprenons les données

		if form.is_valid(): 					# Nous vérifions que les données envoyées sont valides
			form.save()
			return HttpResponseRedirect('/planning/ajout')

	form = SalleForm()  					# Nous créons un formulaire vide
	con = { 'actionAFaire' : 'Ajouter', 'form' : form}

	return render(request,'planning/forms.html', con)

# méthode AJAX ! ! !
def find_planning(request):
	arg = datetime.strptime(request.GET['date'], "%Y-%m-%d")

	debutDeJournee = datetime(arg.year, arg.month, arg.day, 0, 1)
	finDeJournee = datetime(arg.year, arg.month, arg.day, 23, 59)

	res = serializers.serialize(
		"json",
		Soutenance.objects.filter(
			datePassage__lt=finDeJournee,
			datePassage__gt=debutDeJournee
		).order_by('datePassage', 'salle'),
		indent = 2, 
		use_natural_keys=True
	)

	# for itemStage in res:
		# itemStage['fields']['stage'] = serializers.serialize(
		# 	"json",
		# 	Stage.objects.get(pk=itemStage['fields']['stage'])
		# )

	return HttpResponse(res, mimetype="application/json")