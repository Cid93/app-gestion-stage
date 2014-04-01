# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from stage.models import *
from django.shortcuts import render
from django.contrib.auth.models import User


class StageFormEtu(ModelForm):
    etudiant = forms.ModelChoiceField(queryset=Etudiant.objects.all(),
            widget=forms.HiddenInput())
    dateDebut = forms.DateField(widget=SelectDateWidget())
    dateFin = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Stage
        exclude = ['valideOffreStage', 'valideStage']


class StageForm(ModelForm):
    dateDebut = forms.DateField(widget=SelectDateWidget())
    dateFin = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Stage
        exclude = ['valideOffreStage', 'valideStage']


class supprimeStageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(supprimeStageForm, self).__init__(*args, **kwargs)
        self.fields['stageslots'].label = "Selectionnez les stages à supprimer"
    # You can change the queryset in the __init__ method, but this should be a nice basis
        
    stageslots = forms.ModelMultipleChoiceField(queryset=Stage.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)

    def save(self):
        # make sure you do a form.is_valid() before trying to save()
        for stageslot in self.cleaned_data['stageslots']:
            stageslot.delete()
    def list(self):
        # make sure you do a form.is_valid() before trying to save()
        for stageslot in self.cleaned_data['stageslots']:
            print(stageslot)
    class Meta:
        model = Stage
        fields ='stageslots'


class PersonneExtForm(ModelForm):
    class Meta:
        model = PersonneExterieure
        

class OffreStageForm(ModelForm):
    class Meta:
        model = OffreStage
        exclude = ['valideOffreStage']

class supprimeOffreStageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(supprimeOffreStageForm, self).__init__(*args, **kwargs)
        self.fields['offrestagelots'].label = "Selectionnez les offres de stage à supprimer"
    # You can change the queryset in the __init__ method, but this should be a nice basis
        
    offrestagelots = forms.ModelMultipleChoiceField(queryset=OffreStage.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)

    def save(self):
        # make sure you do a form.is_valid() before trying to save()
        for offrestagelots in self.cleaned_data['offrestagelots']:
            offrestagelots.delete()
    def list(self):
        # make sure you do a form.is_valid() before trying to save()
        for offrestagelots in self.cleaned_data['offrestagelots']:
            print(offrestagelots)
    class Meta:
        model = Stage
        fields ='offrestagelots'



class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant


class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant