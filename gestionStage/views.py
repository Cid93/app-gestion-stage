# Create your views here.
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.template import RequestContext
from gestionStage.shortcuts import render

def show_main(request):
	return render(
		request,
		"gestionStage/main.html",
		{})