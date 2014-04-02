# Create your views here.
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.core import serializers
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
		model = request.POST.get('search_data')
		attribut = request.POST.get('select_champ')
		champ = request.POST.get('search_text')
		
		if (model=="Stage" ) and attribut=="entreprise":
			listeEntreprises = Entreprise.objects.filter(nom__contains=champ)
			res = []
			for i in listeEntreprises:
				res += Stage.objects.filter(entreprise=i.idEntreprise, valideStage = True)
			model = get_model('stage', model)

		elif (model=="OffreStage") and attribut=="entreprise":
			listeEntreprises = Entreprise.objects.filter(nom__contains=champ)
			res = []
			for i in listeEntreprises:
				res += OffreStage.objects.filter(entreprise=i.idEntreprise,valideOffreStage=True)
			model = get_model('stage', model)

		elif (model=="Stage") and attribut=="nomLogiciels":
			listeNomLog = Logiciel.objects.filter(nomLog__contains=champ)
			res = []
			for i in listeNomLog:
				res += Stage.objects.filter(nomLogiciels=i.nomLog , valideStage = True)
			model = get_model('stage', model)

		elif (model=="OffreStage") and attribut=="nomLogiciels":
			listeNomLog = Logiciel.objects.filter(nomLog__contains=champ)
			res = []
			for i in listeNomLog:
				res += OffreStage.objects.filter(nomLogiciels=i.nomLog, valideOffreStage=True)
			model = get_model('stage', model)

		elif (model=="OffreStage") and attribut=="intitule":
			res= []
			res = OffreStage.objects.filter(intitule__contains=champ,valideOffreStage=True)
			model = get_model('stage', model)

			
		elif (model=="Stage") and attribut=="intitule":
			res= []
			res = Stage.objects.filter(intitule__contains=champ,valideStage=True)
			model = get_model('stage', model)


		elif (model=="Stage") and attribut=="etudiant":
			listeEtudiant = Etudiant.objects.filter(nom__contains=champ)
			res = []
			for i in listeEtudiant:
				res += Stage.objects.filter(etudiant=i.numEtu , valideStage = True)
			model = get_model('stage', model)
		
		elif (model=="Stage") and attribut=="enseignantTuteur":
			listeEnseignants = Enseignant.objects.filter(nom__contains=champ)
			res = []
			for i in listeEnseignants:
				res += Stage.objects.filter(enseignantTuteur=i.idEnseignant , valideStage = True)
			model = get_model('stage', model)

		elif (model=="Stage") and attribut=="promotion":
			listePromo = Promotion.objects.filter(intitule__contains=champ)
			res = []
			etu = []
			for i in listePromo:
				etu += Etudiant.objects.filter(promotion=i.idPromotion)
			for i in etu:
				res += Stage.objects.filter(etudiant=i.numEtu , valideStage = True)
			model = get_model('stage', model)
		
		elif (model=="Etudiant") and attribut=="promotion":
			listePromo = Promotion.objects.filter(intitule__contains=champ)
			res = []
			for i in listePromo:
				res += Etudiant.objects.filter(promotion=i.idPromotion)
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
                   'Etudiant':('numEtu','nom','prenom','emailEtu','promotion'),
                   'Enseignant':('nom','prenom','emailEns','departement'),
                   'OffreStage':('intitule','entreprise','nomLogiciels'),
                   'Stage':('intitule','entreprise','nomLogiciels','etudiant','enseignantTuteur','promotion')
				  }
	con = { 'data' : type_donnee, "res" : result}			  
	return render(request,"search.html",con)



# méthode AJAX ! ! !
def find_data(request):
	
	
	model = request.GET['model']

	attribut = request.GET['attribut']



	if model== "Entreprise":
		model = get_model('entreprise', model)
	else:
		model = get_model('stage', model)

	res = serializers.serialize(
		"json",
		model.objects.all(),
		indent = 2, 
		use_natural_keys=True
	)

	

	return HttpResponse(res, mimetype="application/json")