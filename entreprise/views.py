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
	try:
		# Vérification des permissions de l'utilisateur
		user = User.objects.get(username=request.user.username)
	except:
		return HttpResponseRedirect('/oups/')
	permissions = user.get_all_permissions()
	
	if ("entreprise.add_entreprise" in permissions):

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

	else:
		return HttpResponseRedirect('/oups')


def modifEnt(request, pk):
	try:
		# Vérification des permissions de l'utilisateur
		user = User.objects.get(username=request.user.username)
	except:
		return HttpResponseRedirect('/oups/')
	permissions = user.get_all_permissions()
	
	if ("entreprise.change_entreprise" in permissions):

		if request.method == 'POST':  # Si on a une requête POST (le formulaire a été posté)
			form = EntrepriseForm(request.POST,instance=Entreprise.objects.get(pk=pk))
			if form.is_valid(): # Nous vérifions que les données envoyées sont valides
				form.save()
				return HttpResponseRedirect('/entreprise/' + pk)
		else: # Si on a une requête GET, on récupère l'id de l'entreprise à modifier et on affiche le form
			form = EntrepriseForm(instance=Entreprise.objects.get(pk=pk))
			print("Error")
			# On crée un formulaire vide

		return render(request,'entreprise/forms.html', { 'actionAFaire' : 'Modifier', 'form' : form})

	else:
		return HttpResponseRedirect('/oups')

def delEnt(request):
	try:
		# Vérification des permissions de l'utilisateur
		user = User.objects.get(username=request.user.username)
	except:
		return HttpResponseRedirect('/oups/')
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
		return HttpResponseRedirect('/oups')