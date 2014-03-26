from django.forms import ModelForm

from planning.models import Soutenance, Salle

class SoutenanceSelection(ModelForm):
    class Meta:
        model = Soutenance
        exclude = ['idSoutenance', 'stage', 'salle']

class SoutenanceForm(ModelForm):
	class Meta:
		model = Soutenance

class SalleForm(ModelForm):
	class Meta:
		model = Salle