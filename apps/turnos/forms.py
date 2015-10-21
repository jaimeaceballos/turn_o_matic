from django.forms import ModelForm
from django import forms
from .models import *


class TipoClienteForm(forms.ModelForm):

	class Meta:
		model 	= TipoCliente
		exclude = []

class ClienteForm(forms.ModelForm):

	class Meta:
		model 	= Cliente 
		exclude = []

class TramitesForm(forms.ModelForm):

	class Meta:
		model 	= Tramites
		exclude = [] 

