# -*- coding: utf-8 -*-
from django.forms import ModelForm, Form, CharField, PasswordInput, Textarea
from django import forms
from stage.models import Stage, Etudiant
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User

class LoginForm(Form):
    username = CharField(max_length=100, label="Identifiant")
    password = CharField(max_length=100, label="Mot de passe", widget=PasswordInput)

def login_page(request):
    context = {}
    context.update(csrf(request))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password= password)
            if user is None:
                context["errmsg"] = "Echec d'authentification"
            elif user.is_active:
                login(request, user)
                return render(request, "gestionStage/main.html", context)
            else:
                context["errmsg"] = "Compte désactivé"
        else:
            context["errmsg"] = "Paramètre non validés"
    else:
        form = LoginForm()
    context["form"] = form
    return render(request, "login.html", context)

def logout_action(request):
    if request.user.is_authenticated():
        logout(request)
        
    return HttpResponseRedirect("/")