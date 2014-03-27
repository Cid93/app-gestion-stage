from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.template import RequestContext
from django.core import serializers

from datetime import datetime

from gestionStage.shortcuts import render
from stage.models import Stage, Etudiant, Enseignant, PersonneExterieure
from planning.models import Soutenance
from planning.forms import SoutenanceSelection, SoutenanceForm, SalleForm

from django.contrib.auth.models import User

import json

def show_planning(request):
	return render(request,
		"planning/planning.html", {
			'form' : SoutenanceForm(),
			'salleForm' : SalleForm()})

def show_soutenance(request, pk):
	return render(
		request,
		"planning/soutenance.html",
		{'soutenance' : Soutenance.objects.get(idSoutenance=pk)})

def addSoutenance(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("planning.add_soutenance" in permissions):

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
	
	else:
		return HttpResponseRedirect('/oups/')


def addSalle(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("planning.add_salle" in permissions):

		if request.method == 'POST':  				# S'il s'agit d'une requête POST
			form = SalleForm(request.POST)  	# Nous reprenons les données

			if form.is_valid(): 					# Nous vérifions que les données envoyées sont valides
				form.save()
				return HttpResponseRedirect('/planning/ajout')

		form = SalleForm()  					# Nous créons un formulaire vide
		con = { 'actionAFaire' : 'Ajouter', 'form' : form}

		return render(request,'planning/forms.html', con)

	else:
		return HttpResponseRedirect('/oups/')

def editSoutenance(request, pk):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("planning.change_soutenance" in permissions):

		if request.method == 'POST':  # S'il s'agit d'une requête POST
			form = SoutenanceForm(request.POST, instance=Soutenance.objects.get(pk=pk))
			if form.is_valid(): # Nous vérifions que les données envoyées sont valides
				form.save()
				return HttpResponseRedirect('/planning/' + pk)
			else: # Si ce n'est pas du POST, c'est probablement une requête GET
				print("Error")

		return render(request,
			'planning/forms.html',
			{ 'actionAFaire' : 'Modifier',
				'form' : SoutenanceForm(instance=Soutenance.objects.get(pk=pk))})

	else:
		return HttpResponseRedirect('/oups/')

# méthode AJAX ! ! !
def find_planning(request):
	debutDeJournee = datetime.strptime(request.GET['dateD'], "%Y-%m-%d");
	finDeJournee = datetime.strptime(request.GET['dateF'], "%Y-%m-%d");

	res = serializers.serialize(
		"json",
		Soutenance.objects.filter(
			datePassage__lt=finDeJournee,
			datePassage__gt=debutDeJournee
		).order_by('datePassage', 'salle'),
		indent = 2, 
		use_natural_keys=True
	)

	return HttpResponse(res, mimetype="application/json")