# Create your views here.
from entreprise.models import Entreprise
from entreprise.forms import EntrepriseForm
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.template import RequestContext

def show_main(request):
	return render_to_response(
		"entreprise/main.html",
		{})

def show_entreprise(request):
	return render_to_response(
		"entreprise/entreprise.html",
		{"liste_entreprise": Entreprise.objects.order_by("nom")})

def show_detail_entreprise(request, pk):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = EntrepriseForm(request.POST,instance=Entreprise.objects.get(pk=pk))
		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()
			return HttpResponseRedirect('/company')
	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = EntrepriseForm(instance=Entreprise.objects.get(pk=pk))
		print("Error")
		  # Nous créons un formulaire vide	
	return render_to_response('entreprise/detail_entreprise.html', {'detail_entreprise' : form}, context_instance=RequestContext(request))


def addEnt(request):

    #entreprise_form = EntrepriseForm()
    #form = EntrepriseForm(instance=Entreprise.objects.all()[1])
    

    if request.method == 'POST':  # S'il s'agit d'une requête POST
    	form = EntrepriseForm(request.POST)  # Nous reprenons les données

    	if form.is_valid(): # Nous vérifions que les données envoyées sont valides
        	form.save()
        	return HttpResponseRedirect('/company')

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
    	form = EntrepriseForm()  # Nous créons un formulaire vide

    return render_to_response('entreprise/addEnt.html', {'entreprise_form' : form}, context_instance=RequestContext(request))
    #return render(request, 'addEnt.html', locals())


def delEnt(request,pk):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = EntrepriseForm(request.POST,instance=Entreprise.objects.get(pk=pk))
		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			Entreprise.objects.get(pk=pk).delete()
			return HttpResponseRedirect('/company')
	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = EntrepriseForm(instance=Entreprise.objects.get(pk=pk)) 
		# Nous créons un formulaire vide	
	return render_to_response('entreprise/delete_entreprise.html', {'delete_entreprise' : form}, context_instance=RequestContext(request))
    

    