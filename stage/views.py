# -*- coding: utf-8 -*-
# Create your views here.
from stage.models import Stage, PersonneExterieure, Etudiant
from stage.forms import StageForm, StageFormEtu, supprimeStageForm, PersonneExtForm
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

def addStage(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.add_stage" in permissions):

		groups = user.groups.all()
		verifEtu = False
		for g in groups:
			if (g.name == "etudiants"):
				verifEtu = True

		if (verifEtu == True):
			etu = Etudiant.objects.get(username=User.objects.get(username=request.user.username))

			if request.method == 'POST': # Si une requête POST a été passée en paramètre
				form = StageFormEtu(request.POST) # On récupère les données
				if form.is_valid(): # Si les données reçues sont valides
					form.save()
					return HttpResponseRedirect('/stage')
				else: # Si les données reçues sont invalides
					con = { 'actionAFaire' : 'Ajouter', 'form' : form,'nomEtu': etu.prenom+' '+etu.nom}
					return render(request,'stage/stage_form.html', con)			

			else: #Si pas de requête
				form = StageFormEtu(initial={'etudiant':etu})
				con = { 'actionAFaire' : 'Ajouter', 'form' : form,'nomEtu': etu.prenom+' '+etu.nom}

				return render(request,'stage/stage_form.html', con)

		else:
			if request.method == 'POST': # Si une requête POST a été passée en paramètre
				form = StageForm(request.POST) # On récupère les données
				
				if form.is_valid(): # Si les données reçues sont valides
					form.save()
					return HttpResponseRedirect('/stage')
				else: # Si les données reçues sont invalides
					con = { 'actionAFaire' : 'Ajouter', 'form' : form}
					return render(request,'stage/stage_form.html', con)			

			else: #Si pas de requête
				form = StageForm()
				con = { 'actionAFaire' : 'Ajouter', 'form' : form}

				return render(request,'stage/stage_form.html', con)

	else:
		return HttpResponseRedirect('/oups/')
	

def modifStage(request, pk):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.change_stage" in permissions):

		groups = user.groups.all()
		verifEtu = False
		for g in groups:
			if (g.name == "etudiants"):
				verifEtu = True

		stg = Stage.objects.get(pk=pk)

		if (verifEtu):
			etu = Etudiant.objects.get(username=User.objects.get(username=request.user.username))

			if stg.etudiant != etu:
				return HttpResponseRedirect('/stage/monStage/')

			if request.method == 'POST': # Si une requête POST a été passée en paramètre
				form = StageFormEtu(request.POST, instance=stg) # On récupère les données

				if form.is_valid() : # Si les données reçues sont valides
					form.save()
					return HttpResponseRedirect('/stage/' + pk)
				else: # Si les données reçues sont invalides
					con = { 'actionAFaire' : 'Modifier', 'form' : form,'nomEtu': etu.prenom+' '+etu.nom}
					return render(request,'stage/stage_form.html', con)			

			else: #Si pas de requête
				form = StageFormEtu(instance=Stage.objects.get(pk=pk))
				con = { 'actionAFaire' : 'Modifier', 'form' : form,'nomEtu': etu.prenom+' '+etu.nom}

		else:
			if request.method == 'POST': # Si une requête POST a été passée en paramètre
				form = StageForm(request.POST, instance=stg) # On récupère les données
				
				if form.is_valid(): # Si les données reçues sont valides
					form.save()
					return HttpResponseRedirect('/stage/' + pk)
				else: # Si les données reçues sont invalides
					con = { 'actionAFaire' : 'Modifier', 'form' : form}
					return render(request,'stage/stage_form.html', con)			

			else: #Si pas de requête
				form = StageForm(instance=Stage.objects.get(pk=pk))
				con = { 'actionAFaire' : 'Modifier', 'form' : form}

		return render(request,'stage/stage_form.html', con)

	else:
		return HttpResponseRedirect('/oups/')


def delStage(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.delete_stage" in permissions):
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
	else:
		con = {}
		return HttpResponseRedirect('/oups/')
		#return render(request,'stage/oops.html', con)
		

def monStage(request):
	try:
		stgs = Stage.objects.filter(
			etudiant=Etudiant.objects.get(
				username=User.objects.get(
					username=request.user.username)))
		monStg = None

		for stg in stgs:
			if monStg == None:
				monStg = stg
				continue
			if stg.idStage > monStg.idStage:
				monStg = stg

		return show_detail_stage(
			request,
			monStg.idStage
		)
	except:
		return addStage(request)
		

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