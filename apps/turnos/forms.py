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
		
class SectoresForm(forms.ModelForm):

         class Meta:
                  model    = Sectores
                  exclude  = []		

class BoxAtencionForm(forms.ModelForm):

	class Meta:
		model 	= BoxAtencion
		exclude = [] 		


class AutoForm(forms.ModelForm):

	class Meta:

		model = Auto
		exclude = []

class TurnosForm(forms.ModelForm): #patty

	class Meta:
		model   = Turnos
		exclude =[]

class SolicitarForm(forms.Form):
	tramite 		= forms.ModelChoiceField(queryset=Tramites.objects.all(),empty_label=None)
	documento 		= forms.CharField(max_length=10)
