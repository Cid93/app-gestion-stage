from django import forms
from django.forms import ModelForm

from planning.models import Soutenance, Salle
from stage.models import Stage

class SoutenanceSelection(ModelForm):
    class Meta:
        model = Soutenance
        exclude = ['idSoutenance', 'stage', 'salle']

class SoutenanceForm(ModelForm):
    stage = forms.ModelChoiceField(queryset=Stage.objects.filter(valideStage=True))

    class Meta:
        model = Soutenance

class SalleForm(ModelForm):
	class Meta:
		model = Salle

class supprimerSoutenanceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(supprimerSoutenanceForm, self).__init__(*args, **kwargs)
        self.fields['soutenanceslots'].label = "Selectionnez les soutenances à supprimer"
    # You can change the queryset in the __init__ method, but this should be a nice basis
        
    soutenanceslots = forms.ModelMultipleChoiceField(
        queryset=Soutenance.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False)

    def save(self):
        # make sure you do a form.is_valid() before trying to save()
        for soutenance in self.cleaned_data['soutenanceslots']:
            soutenance.delete()
    def list(self):
        # make sure you do a form.is_valid() before trying to save()
        for soutenance in self.cleaned_data['soutenanceslots']:
            print(soutenance)

    class Meta:
        model = Soutenance
        fields ='soutenanceslots'