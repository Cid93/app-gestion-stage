from django.core.management import setup_environ
from gestionStage import settings
setup_environ(settings)

from entreprise.models import Entreprise

import json

entreprise = json.load(open("entreprise.json",encoding="utf-8"))


for e in entreprise:
	company = Entreprise(nom=e["nom"],adresse=e["adresse"],codePostal=e["codePostal"],ville=e["ville"],pays=e["pays"],telephone=e["telephone"],fax=e["fax"])
	company.save()



	

