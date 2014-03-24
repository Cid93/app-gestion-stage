# -*- coding: utf-8 -*-
# Create your views here.
from entreprise.models import Entreprise
from entreprise.forms import EntrepriseForm
from django.shortcuts import HttpResponseRedirect, HttpResponse
from gestionStage.shortcuts import render
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf
from entreprise.forms import supprimeEntrepriseForm
from django.contrib.auth.models import User


# Shows
def show_main(request):
	return render(
		request,
		"entreprise/main.html",
		{})

def show_entreprise(request):
	return render(
		request,
		"entreprise/entreprise.html",
		{"liste_entreprise": Entreprise.objects.order_by("nom")})

def show_detail_entreprise(request, pk):
	return render(
		request,
		"entreprise/detail_entreprise.html",
		{"entreprise": Entreprise.objects.get(pk=pk)})

def show_visiter(request):
	return render(
		request,
		"entreprise/visite_entreprise.html",
		{"liste_entreprise": Entreprise.objects.order_by("nom")})

# Manipulation Entreprise
def addEnt(request):
	if request.method == 'POST':  				# Si une requête POST a été passée
		form = EntrepriseForm(request.POST)  	# On récupère les données
		
		if form.is_valid(): 					# Si les données reçues sont valides
			form.save()
			return HttpResponseRedirect('/entreprise')
		else:									# Si les données reçues sont invalides
			con = { 'actionAFaire' : 'Ajouter', 'form' : form}
			return render(request,'entreprise/forms.html', con)

	else: 										# Pas de requête POST
		form = EntrepriseForm()  				# On crée un formulaire vide
		con = { 'actionAFaire' : 'Ajouter', 'form' : form}
		return render(request,'entreprise/forms.html', con)


def modifEnt(request, pk):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = EntrepriseForm(request.POST,instance=Entreprise.objects.get(pk=pk))
		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()
			return HttpResponseRedirect('/entreprise/' + pk)
	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = EntrepriseForm(instance=Entreprise.objects.get(pk=pk))
		print("Error")
		  # Nous créons un formulaire vide

	return render(request,'entreprise/forms.html', { 'actionAFaire' : 'Modifier', 'form' : form})


def delEnt(request):
	# Vérification des permissions de l'utilisateur
	user = User.objects.get(username=request.user.username)
	permissions = user.get_all_permissions()
	
	if ("entreprise.delete_entreprise" in permissions):
		supprimeentrepriseform = supprimeEntrepriseForm()
		con ={'form': supprimeentrepriseform, 'actionAFaire' : 'Supprimer'}
		con.update(csrf(request))
		if len(request.POST) > 0:
			supprimeentrepriseform =supprimeEntrepriseForm(request.POST)
			con = {'form': supprimeentrepriseform}
			if supprimeentrepriseform.is_valid():   
				supprimeentrepriseform.save()
				return HttpResponseRedirect("/entreprise/")
		else:
			return render(request,'entreprise/forms.html', con)

	else:
		con = {}
		return HttpResponseRedirect('/oups')