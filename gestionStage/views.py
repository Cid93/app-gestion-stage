# Create your views here.
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm

from django.template import RequestContext
from gestionStage.shortcuts import render
from django.db.models import get_model
from entreprise.models import Entreprise
from stage.models import *

def show_main(request):
	return render(
		request,
		"gestionStage/main.html",
		{})

def oups(request):
	return render(
		request,
		"oups.html",
		{})

def search(request):
	if request.method == 'POST':
		# Requete :
		# csrfmiddlewaretoken=S1conZBXfCETKe0bh2rM2HOk7h9V4CZd
		# &search_data=Etudiant
		# &select_champ=numEtu
		# &search_text=atos


		model = request.POST.get('search_data')
		attribut = request.POST.get('select_champ')
		champ = request.POST.get('search_text')
		

		if (model=="Stage" or model=="OffreStage") and attribut=="entreprise":
			
			listeEntreprises = Entreprise.objects.filter(nom__contains=champ)
			res = []
			for i in listeEntreprises:
				res += Stage.objects.filter(entreprise=i.idEntreprise)
			model = get_model('stage', model)
		elif (model=="Stage" or model=="OffreStage") and attribut=="nomLogiciels":
			listeNomLog = Logiciel.objects.filter(nomLog__contains=champ)
			print(listeNomLog)
			res = []
			for i in listeNomLog:
				print(i)
				res += Stage.objects.filter(nomLogiciels=i.nomLog)
			model = get_model('stage', model)
		elif (model=="Stage") and attribut=="etudiant":
			listeEtudiant = Etudiant.objects.filter(nom__contains=champ)
			res = []
			for i in listeEtudiant:
				res += Stage.objects.filter(etudiant=i.numEtu)
			model = get_model('stage', model)
		elif (model=="Stage") and attribut=="enseignantTuteur":
			listeEnseignants = Enseignant.objects.filter(nom__contains=champ)
			res = []
			for i in listeEnseignants:
				res += Stage.objects.filter(enseignantTuteur=i.idEnseignant)
			model = get_model('stage', model)
		else:
			column = attribut+'__contains'
			kwargs = {
				column : champ
			}
			
			if model== "Entreprise":
				model = get_model('entreprise', model)
			else:
				model = get_model('stage', model)

			res=model.objects.filter(**kwargs)



		# Construction du tableau de résultats
		result = model.search_result_header()
		result+= '<tbody>'
		for i in res:
			result += i.search_result()
		result += '</tbody>'
		

	else:
		result = None


	

	type_donnee = {'Entreprise':('nom','ville','pays'),
                   'Etudiant':('numEtu','nom','prenom','emailEtu'),
                   'Enseignant':('nom','prenom','emailEns','departement'),
                   'OffreStage':('intitule','entreprise','nomLogiciels'),
                   'Stage':('intitule','entreprise','nomLogiciels','etudiant','enseignantTuteur','promotion')
				  }
	con = { 'data' : type_donnee, "res" : result}			  
	return render(request,"search.html",con)