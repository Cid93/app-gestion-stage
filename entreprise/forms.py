from django.forms import ModelForm
from django import forms
from entreprise.models import Entreprise

class EntrepriseForm(ModelForm):
    class Meta:
        model = Entreprise

class supprimeEntrepriseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(supprimeEntrepriseForm, self).__init__(*args, **kwargs)
        self.fields['entrepriseslots'].label = "selectionnez les entreprises à supprimer"
    # You can change the queryset in the __init__ method, but this should be a nice basis
        
    entrepriseslots = forms.ModelMultipleChoiceField(queryset=Entreprise.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)


    def save(self):
        # make sure you do a form.is_valid() before trying to save()
        for entrepriseslot in self.cleaned_data['entrepriseslots']:
            entrepriseslot.delete()
    def list(self):
        # make sure you do a form.is_valid() before trying to save()
        for entrepriseslot in self.cleaned_data['entrepriseslots']:
            print(entrepriseslot)
    class Meta:
        model = Entreprise
        fields ='entrepriseslots'

