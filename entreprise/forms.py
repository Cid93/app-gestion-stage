from django.forms import ModelForm
from entreprise.models import Entreprise

class EntrepriseForm(ModelForm):
    class Meta:
        model = Entreprise


