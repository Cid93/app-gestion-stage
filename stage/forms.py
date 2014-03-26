# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from stage.models import Stage, PersonneExterieure, Etudiant
from django.shortcuts import render
from django.contrib.auth.models import User


class StageFormEtu(ModelForm):
    etudiant = forms.ModelChoiceField(queryset=Etudiant.objects.all(),
            widget=forms.HiddenInput())

    class Meta:
        model = Stage


class StageForm(ModelForm):
    class Meta:
        model = Stage


class supprimeStageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(supprimeStageForm, self).__init__(*args, **kwargs)
        self.fields['stageslots'].label = "selectionnez les stages à supprimer"
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
        
