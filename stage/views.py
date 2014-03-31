# -*- coding: utf-8 -*-
# Create your views here.
from stage.models import OffreStage, Stage, PersonneExterieure, Etudiant
from stage.forms import *
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
					return HttpResponseRedirect('/stage/ok')
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
					return HttpResponseRedirect('/stage/ok')
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



def showOffres(request):
	return render(
		request,
		"offrestage/offrestage.html",
		{"liste_offrestage": OffreStage.objects.order_by("intitule")}
	)

def detailsOffreStage(request, pk):
	return render(
		request,
		"offrestage/details_offrestage.html",
		{"offrestage": OffreStage.objects.get(pk=pk)}
	)

def addOffreStage(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.add_offrestage" in permissions):

		if request.method == 'POST':  				# Si une requête POST a été passée
			form = OffreStageForm(request.POST)  	# On récupère les données
			
			if form.is_valid(): 					# Si les données reçues sont valides
				form.save()
				return HttpResponseRedirect('/stage/offrestage/ok')
			else:									# Si les données reçues sont invalides
				con = { 'actionAFaire' : 'Ajouter', 'form' : form}
				return render(request,'offrestage/forms.html', con)

		else: 										# Pas de requête POST
			form = OffreStageForm()  				# On crée un formulaire vide
			con = { 'actionAFaire' : 'Ajouter', 'form' : form}
			return render(request,'offrestage/forms.html', con)

	else:
		return HttpResponseRedirect('/oups/')


def modifOffreStage(request, pk):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.change_offrestage" in permissions):

		if request.method == 'POST':  # Si on a une requête POST (le formulaire a été posté)
			form = OffreStageForm(request.POST,instance=OffreStage.objects.get(pk=pk))
			if form.is_valid(): # Nous vérifions que les données envoyées sont valides
				form.save()
				return HttpResponseRedirect('/stage/offrestage/' + pk)
		else: # Si on a une requête GET, on récupère l'id de l'entreprise à modifier et on affiche le form
			form = OffreStageForm(instance=OffreStage.objects.get(pk=pk))
			print("Error")
			# On crée un formulaire vide

		return render(request,'offrestage/forms.html', { 'actionAFaire' : 'Modifier', 'form' : form})

	else:
		return HttpResponseRedirect('/oups')


def delOffreStage(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.delete_offrestage" in permissions):
		form = supprimeOffreStageForm()
		con ={'form': form, 'actionAFaire' : 'Supprimer'}
		con.update(csrf(request))
		if len(request.POST) > 0:
			form =supprimeOffreStageForm(request.POST)
			con = {'form': form}
			if form.is_valid():   
				form.save()
				return HttpResponseRedirect("/stage/offrestage")
		else:
			return render(request,'offrestage/forms.html', con)

	else:
		return HttpResponseRedirect('/oups')


# def validerOffreStage(request):
# 	# Vérification des permissions de l'utilisateur
# 	user = User.objects.get(username=request.user.username)
# 	permissions = user.get_all_permissions()
	
# 	if ("stage.valider_offrestage" in permissions):
# 		form = validerOffreStageForm()
# 		con ={'form': form, 'actionAFaire' : 'Valider'}
# 		con.update(csrf(request))
# 		if len(request.POST) > 0:
# 			form =validerOffreStageForm(request.POST)
# 			con = {'form': form}
# 			if form.is_valid():   
# 				form.save()
# 				return HttpResponseRedirect("/stage/offrestage")
# 		else:
# 			return render(request,'offrestage/forms.html', con)

# 	else:
# 		return HttpResponseRedirect('/oups')

def validerOffreStage(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("stage.valider_offrestage" in permissions):
		return render(
			request,
			"offrestage/valideroffrestage.html",
			{"liste_offrestage": OffreStage.objects.order_by("intitule")}
		)

	else:
		return HttpResponseRedirect('/oups')


def detailsEtudiant(request, pk):
	return render(
		request,
		"etudiant/details_etudiant.html",
		{"etudiant": Etudiant.objects.get(pk=pk)}
	)

def modifEtudiant(request, pk):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	etudiant = Etudiant.objects.get(pk=pk)

	if ("stage.change_etudiant" in permissions or etudiant.username == user):


		if request.method == 'POST':  # Si on a une requête POST (le formulaire a été posté)
			form = EtudiantForm(request.POST,instance=Etudiant.objects.get(pk=pk))
			if form.is_valid(): # Nous vérifions que les données envoyées sont valides
				form.save()
				return HttpResponseRedirect('/etudiant/' + pk)
		else: # Si on a une requête GET, on récupère l'id de l'entreprise à modifier et on affiche le form
			form = EtudiantForm(instance=Etudiant.objects.get(pk=pk))
			print("Error")
			# On crée un formulaire vide

		return render(request,'etudiant/forms.html', { 'actionAFaire' : 'Modifier', 'form' : form})

	else:
		return HttpResponseRedirect('/oups')

def detailsEnseignant(request, pk):
	return render(
		request,
		"enseignant/details_enseignant.html",
		{"enseignant": Enseignant.objects.get(pk=pk)}
	)

def modifEnseignant(request, pk):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	enseignant = Enseignant.objects.get(pk=pk)

	if ("stage.change_enseignant" in permissions or enseignant.username == user):


		if request.method == 'POST':  # Si on a une requête POST (le formulaire a été posté)
			form = EnseignantForm(request.POST,instance=Enseignant.objects.get(pk=pk))
			if form.is_valid(): # Nous vérifions que les données envoyées sont valides
				form.save()
				return HttpResponseRedirect('/enseignant/' + pk)
		else: # Si on a une requête GET, on récupère l'id de l'entreprise à modifier et on affiche le form
			form = EnseignantForm(instance=Enseignant.objects.get(pk=pk))
			print("Error")
			# On crée un formulaire vide

		return render(request,'enseignant/forms.html', { 'actionAFaire' : 'Modifier', 'form' : form})

	else:
		return HttpResponseRedirect('/oups')


def monProfilEtu(request):

	etu = Etudiant.objects.filter(
			username=User.objects.get(
				username=request.user.username))
	monProfil = None

	for e in etu:
		monProfil = e.numEtu

	return detailsEtudiant(
		request,
		monProfil
	)

def monProfilEns(request):

	ens = Enseignant.objects.filter(
			username=User.objects.get(
				username=request.user.username))
	monProfil = None

	for e in ens:
		monProfil = e.idEnseignant

	return detailsEnseignant(
		request,
		monProfil
	)
	
def offreStage_operationEffectuee(request):
	return render(
		request,
		"offrestage/operation_effectuee.html",
		{}
	)

def stage_operationEffectuee(request):
	return render(
		request,
		"stage/operation_effectuee.html",
		{}
	)