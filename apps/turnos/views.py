from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

# Create your views here.


def home (request):
		
	values={}
	return render_to_response('index.html',values,context_instance = RequestContext(request))

def tipo_cliente(request):
	listado = TipoCliente.objects.all()

	values = {
		'listado' : listado
	}
	return render_to_response('turnos/tipo_cliente.html',values,context_instance = RequestContext(request))

def tipo_cliente_nuevo(request):
	tipo_cliente 	= TipoClienteForm()

	values = {
		'tipo_cliente' : tipo_cliente,
	}

	return render_to_response('turnos/tipo_cliente_nuevo.html',values,context_instance = RequestContext(request))

def tipo_cliente_save(request):
	if request.method == 'POST':
		tipo_cliente = TipoClienteForm(request.POST)
		if tipo_cliente.is_valid():
			tipo_cliente.save()
			return HttpResponseRedirect(reverse('tipo_cliente'))	
		else:
			values = {
				'tipo_cliente' : tipo_cliente,
				'errors'	   : tipo_cliente.errors,
			}
			return render_to_response('turnos/tipo_cliente_nuevo.html',values,context_instance = RequestContext(request))			
	return HttpResponseRedirect(reverse('tipo_cliente'))		

def tipo_cliente_delete(request,id):
	tipo_cliente = TipoCliente.objects.get(id=id)
	tipo_cliente.delete()
	return HttpResponseRedirect(reverse('tipo_cliente'))	

def tipo_cliente_edit(request,id):
	tipo_cliente 	= TipoClienteForm(instance=TipoCliente.objects.get(id=id))
	print tipo_cliente
	if request.method == 'POST':
		tipo_cliente = TipoClienteForm(request.POST)
		if tipo_cliente.is_valid():
			t_cliente = TipoCliente.objects.get(id=id)
			t_cliente.tipo = tipo_cliente.cleaned_data['tipo']
			t_cliente.save()
			return HttpResponseRedirect(reverse('tipo_cliente'))	
		else:
			values = {
				'tipo_cliente' : tipo_cliente,
				'errors'	   : tipo_cliente.errors,
			}
			return render_to_response('turnos/tipo_cliente_edit.html',values,context_instance = RequestContext(request))
	values = {
		'tipo_cliente' : tipo_cliente,
		'id' : id,
	}
	return render_to_response('turnos/tipo_cliente_edit.html',values,context_instance = RequestContext(request))