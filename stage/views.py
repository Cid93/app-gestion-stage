# -*- coding: utf-8 -*-
# Create your views here.
from stage.models import Stage, PersonneExterieure, Etudiant
from stage.forms import StageForm, supprimeStageForm, PersonneExtForm
from django.shortcuts import HttpResponseRedirect, HttpResponse
from gestionStage.shortcuts import render
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
#from stage.forms import supprimeStageForm

def show_stages(request):
	return render(
		request,
		"stage/stage.html",
		{"liste_stage": Stage.objects.order_by("intitule")})

def show_detail_stage(request, pk):
	return render(
		request,
		"stage/detail_stage.html",
		{"stage": Stage.objects.get(pk=pk)}
		)

# Manipulation Entreprise
def addStage(request):
	if request.method == 'POST': # Si une requête POST a été passée en paramètre
		form = StageForm(request.POST) # On récupère les données

		if form.is_valid(): # Si les données reçues sont valides
			form.save()
			return HttpResponseRedirect('/stage')
		else: # Si les données reçues sont invalides
			con = { 'actionAFaire' : 'Ajouter', 'form' : form}
			return render(request,'stage/add_stage.html', con)			

	else: #Si pas de requête
		form = StageForm()  # Nous créons un formulaire vide
		con = { 'actionAFaire' : 'Ajouter', 'form' : form}

		return render(request,'stage/add_stage.html', con)
	

def modifStage(request, pk):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = StageForm(request.POST,instance=Stage.objects.get(pk=pk))
		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()
			return HttpResponseRedirect('/stage/' + pk)
	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = StageForm(instance=Stage.objects.get(pk=pk))
		print("Error")
		  # Nous créons un formulaire vide

	return render(request,'stage/forms.html', 
							{ 'actionAFaire' : 'Modifier', 'form' : form})

def delStage(request):
 
    supprimestageform = supprimeStageForm()
    con ={'form': supprimestageform, 'actionAFaire' : 'Supprimer'}
    con.update(csrf(request))
    if len(request.POST) > 0:
        supprimestageform =supprimeStageForm(request.POST)
        con = {'form': supprimestageform}
        if supprimestageform.is_valid():  
            supprimestageform.save()
            return HttpResponseRedirect("/stage/")
    else:
        return render(request,'stage/forms.html', con)

def monStage(request):
	try:
		return render(
			request,
			"stage/detail_stage.html",
			{"stage": Stage.objects.get(
						etudiant=Etudiant.objects.get(
							username=User.objects.get(
								username=request.user.username)))}
			)
	except :
		return render(request,
			'stage/forms.html',
			{ 'actionAFaire' : 'Ajouter',
				'form' : StageForm()})

# Manipulation Personnes extérieures
def addPersonneExt(request):
	if request.method == 'POST':  				# S'il s'agit d'une requête POST
		form = PersonneExtForm(request.POST)  	# Nous reprenons les données

		if form.is_valid(): 					# Nous vérifions que les données envoyées sont valides
			form.save()
			return HttpResponseRedirect('/stage/ajouter')

	form = PersonneExtForm()  					# Nous créons un formulaire vide
	con = { 'actionAFaire' : 'Ajouter', 'form' : form}

	return render(request,'stage/forms.html', con)