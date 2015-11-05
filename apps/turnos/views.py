from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
import datetime
from .models import *
from .forms import *

# Create your views here.

# Vista que renderiza el home
def home (request):
		
	values={} 										# Genero un diccionario de datos vacio para pasarlo al contexto
	return render_to_response('index.html',values,context_instance = RequestContext(request)) # devuelvo al backend el template que debe renderizar con el contexto

def vista_cliente(request):
	solicitar 		= SolicitarForm()

	values = {
		'form' : solicitar,
	}
	return render_to_response('turnos/solicitar.html',values,context_instance = RequestContext(request)) # devuelvo al backend el template que debe renderizar con el contexto

def solicita_turno(request):
	if request.method == "POST":
		solicitar 	= SolicitarForm(request.POST)
		if solicitar.is_valid():
			tramite 	= solicitar.cleaned_data['tramite']
			codigo_sector = tramite.sector
			ultimo_turno 	= Turnos.objects.filter(sector=codigo_sector).order_by('-id')[:1]
			if ultimo_turno and ultimo_turno[0].numero < 999:
				numero = ultimo_turno[0].numero + 1
			else:
				numero = 1
			turno = Turnos()
			try:
				cliente 	= Cliente.objects.get(dni=solicitar.cleaned_data['documento'])
				turno.cliente = cliente				
			except:
				turno.no_cliente 	= solicitar.cleaned_data['documento']
			finally:
				turno.sector = codigo_sector
				turno.numero = numero
				turno.fecha = datetime.datetime.now()
				turno.estado = "ESPERA"				
				turno.save()			
			values = {
				'turno' : turno,
			}
			return render_to_response('turnos/turno_ok.html',values,context_instance = RequestContext(request))
	return HttpResponseRedirect(reverse('vista_cliente'))

def ultimos_turnos(request):
	ultimos_turnos = Turnos.objects.all().order_by('-id')[:5]
	values = {
		'ultimos_turnos' : ultimos_turnos,
	}
	return render_to_response('turnos/ultimos_turnos.html',values,context_instance = RequestContext(request))

# vista que maneja la pantalla de tipos de clientes
def tipo_cliente(request):
	listado = TipoCliente.objects.all() 			# obtengo de la base de datos un listado de tipo de clientes

	values = { 										# genero un diccionario de datos
		'listado' : listado 						# agrego el listado al diccionario
	}
	return render_to_response('turnos/tipo_cliente.html',values,context_instance = RequestContext(request))

# vista que maneja la creacion de un nuevo tipo de cliente
def tipo_cliente_nuevo(request):
	tipo_cliente 	= TipoClienteForm() 			# genero un nuevo formulario de tipo de clientes

	values = { 										# genero el diccionario de datos
		'tipo_cliente' : tipo_cliente, 				# agrego el formulario al diccionario
	}

	return render_to_response('turnos/tipo_cliente_nuevo.html',values,context_instance = RequestContext(request))

# vista que maneja el grabar un nuevo tipo de cliente
def tipo_cliente_save(request):
	if request.method == 'POST': 									# si la peticion es por el metodo post
		tipo_cliente = TipoClienteForm(request.POST) 				# obtengo el formulario desde el frontend
		if tipo_cliente.is_valid(): 								# si el formulario es valido
			tipo_cliente.save() 									# guardo en la base de datos
			return HttpResponseRedirect(reverse('tipo_cliente'))	# luego de guardar vuelvo a la pantalla de tipos de cliente
		else:														# si no es valido el formulario
			values = { 												# genero un diccionario
				'tipo_cliente' : tipo_cliente, 						# le agrego el formulario obtenido desde el frontend
				'errors'	   : tipo_cliente.errors, 				# agrego los errores
			}
			return render_to_response('turnos/tipo_cliente_nuevo.html',values,context_instance = RequestContext(request))			
	return HttpResponseRedirect(reverse('tipo_cliente'))			# si el metodo no es post, vuelvo a la pantalla de tipos de clientes

# vista que maneja la eliminacion de un tipo de clientes
def tipo_cliente_delete(request,id):
	tipo_cliente = TipoCliente.objects.get(id=id) 					# obtengo el registro de la base de datos en un objeto de tipo_cliente
	tipo_cliente.delete()											# borro el objeto
	return HttpResponseRedirect(reverse('tipo_cliente'))			# vuelvo a la pagina de tipos de cliente

# vista que maneja la edicion del usuario
def tipo_cliente_edit(request,id):
	tipo_cliente 	= TipoClienteForm(instance=TipoCliente.objects.get(id=id)) 	# obtengo un formulario instanciado con el registro de la base de datos
	if request.method == 'POST':												# si la peticion llega por post
		tipo_cliente = TipoClienteForm(request.POST) 							# obtengo el formulario desde el contexto
		if tipo_cliente.is_valid(): 											# si el formulario es valido
			t_cliente = TipoCliente.objects.get(id=id)							# obtengo el objeto de la base de datos
			t_cliente.tipo = tipo_cliente.cleaned_data['tipo']					# asigno el nuevo valor al objeto
			t_cliente.save() 													# guardo el objeto en la base de datos con el nuevo valor
			return HttpResponseRedirect(reverse('tipo_cliente'))				# retorno a la pantalla de tipo cliente
		else: 																	#
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

def cliente(request):
	listado 	= Cliente.objects.all()
	values={
		'listado' : listado,
	}

	return render_to_response('turnos/cliente.html',values,context_instance = RequestContext(request))

def cliente_nuevo(request):
	cliente 	= ClienteForm()

	values = {
		'cliente':cliente,
	}
	return render_to_response('turnos/cliente_nuevo.html',values,context_instance=RequestContext(request))

def cliente_save(request):
	if request.method == 'POST':
		cliente = ClienteForm(request.POST)
		if cliente.is_valid():
			cliente.save()
			
		else:
			values = {
				'cliente' : cliente,
				'errors'  : cliente.errors,
			}
			return render_to_response('turnos/cliente_nuevo.html',values,context_instance=RequestContext(request))
	return HttpResponseRedirect(reverse('cliente'))

def cliente_edit(request,id):
	cliente = ClienteForm(instance=Cliente.objects.get(id=id))
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			cliente = Cliente.objects.get(id=id)
			cliente.tipo_cliente 	= form.cleaned_data['tipo_cliente']
			cliente.dni 			= form.cleaned_data['dni']
			cliente.nombre 			= form.cleaned_data['nombre']
			cliente.save()
			return HttpResponseRedirect(reverse('cliente'))
	values = {
		'cliente' : cliente,
		'id' 	  : id,
	}

	return render_to_response('turnos/cliente_edit.html',values,context_instance=RequestContext(request))

def cliente_delete(request,id):
	cliente = Cliente.objects.get(id=id)
	cliente.delete()
	return HttpResponseRedirect(reverse('cliente'))

def tramites(request):
	listado = Tramites.objects.all()

	values = {
		'listado' : listado
	}
	return render_to_response('turnos/tramite.html',values,context_instance=RequestContext(request))

def tramite_nuevo(request):
	tramite 	= TramitesForm()

	values = {
		'tramite':tramite,
	}

	return render_to_response('turnos/tramite_nuevo.html',values,context_instance=RequestContext(request))

def tramite_save(request):
	if request.method == 'POST':
		tramite = TramitesForm(request.POST)
		if tramite.is_valid():
			tramite.save()
			
		else:
			values = {
				'tramite' : tramite,
				'errors'  : tramite.errors,
			}
			return render_to_response('turnos/tramite_nuevo.html',values,context_instance=RequestContext(request))
	return HttpResponseRedirect(reverse('tramite'))

def tramite_edit(request,id):
	tramite = TramitesForm(instance=Tramites.objects.get(id=id))
	if request.method == 'POST':
		form = TramitesForm(request.POST)
		if form.is_valid():
			tramite = Tramites.objects.get(id=id)
			tramite.descripcion			= form.cleaned_data['descripcion']
			tramite.save()
			return HttpResponseRedirect(reverse('tramite'))
	values = {
		'tramite' : tramite,
		'id' 	  : id,
	}

	return render_to_response('turnos/tramite_edit.html',values,context_instance=RequestContext(request))

def tramite_delete(request,id):
	tramite = Tramites.objects.get(id=id)
	tramite.delete()
	return HttpResponseRedirect(reverse('tramite'))
	


def boxAtencion(request):
	boxAtencion = BoxAtencion.objects.all()

	values = {
		'boxAtencion' : boxAtencion
	}
	return render_to_response('turnos/boxAtencion.html',values,context_instance=RequestContext(request))

def boxAtencion_nuevo(request):
	boxAtencion 	= BoxAtencionForm()

	values = {
		'boxAtencion':boxAtencion,
	}

	return render_to_response('turnos/boxAtencion_nuevo.html',values,context_instance=RequestContext(request))
# vista que maneja la creacion de un nuevo tipo de cliente

def boxAtencion_save(request):
	if request.method == 'POST':
		boxAtencion = BoxAtencionForm(request.POST)
		if boxAtencion.is_valid():
			boxAtencion.save()
			
		else:
			values = {
				'boxAtencion' : boxAtencion,
				'errors'  : boxAtencion.errors,
			}
			return render_to_response('turnos/boxAtencion_nuevo.html',values,context_instance=RequestContext(request))
	return HttpResponseRedirect(reverse('boxAtencion'))

def boxAtencion_edit(request,id):
	boxAtencion = BoxAtencionForm(instance=BoxAtencion.objects.get(id=id))
	if request.method == 'POST':
		form = BoxAtencionForm(request.POST)
		if form.is_valid():
			boxAtencion = BoxAtencion.objects.get(id=id)
			boxAtencion.nro_box 	= form.cleaned_data['nro_box']
			boxAtencion.empleado			= form.cleaned_data['empleado']
			boxAtencion.sectores 			= form.cleaned_data['sectores']
			boxAtencion.habilitado 			= form.cleaned_data['habilitado']
			boxAtencion.save()
			return HttpResponseRedirect(reverse('boxAtencion'))
	values = {
		'boxAtencion' : boxAtencion,
		'id' 	  : id,
	}
	return render_to_response('turnos/boxAtencion_edit.html',values,context_instance=RequestContext(request))

def boxAtencion_delete(request,id):
	boxAtencion = BoxAtencion.objects.get(id=id)
	boxAtencion.delete()
	return HttpResponseRedirect(reverse('boxAtencion'))


def auto_nuevo(request):
	form = AutoForm()

	values = {
		'form' : form,
	}

	return render_to_response('auto_nuevo.html',values,context_instance=RequestContext(request))

def auto_save(request):
	if request.method == 'POST':
		form = AutoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('auto_nuevo'))

	form = AutoForm()

	values = {
		'form' : form,
	}

	return render_to_response('auto.html',values,context_instance=RequestContext(request))

def auto_edit(request,id):
	objeto_auto = Auto.objects.get(id=id)
	auto = AutoForm(instance=objeto_auto)
	if request.method == 'POST':
		form = AutoForm(request.POST)
		if form.is_valid():
			objeto_auto.patente			= form.cleaned_data['patente']
			objeto_auto.marca_modelo		= form.cleaned_data['marca_modelo']
			objeto_auto.save()
			return HttpResponseRedirect(reverse('auto_nuevo'))
	values = {
		'form' : auto,
		'id' 	  : id,
	}

	return render_to_response('auto_edit.html',values,context_instance=RequestContext(request))

def auto(request):
	listado = Auto.objects.all()
	values = {
		'listado' : listado,
	}
	return render_to_response('auto.html',values,context_instance=RequestContext(request))	

def auto_delete(request,id):
	auto = Auto.objects.get(id=id)
	auto.delete()
	return HttpResponseRedirect(reverse('auto'))

	
def sector_nuevo(request):
	sector 	= SectoresForm()

	values = {
		'sector':sector,
	}

	return render_to_response('turnos/sector_nuevo.html',values,context_instance=RequestContext(request))
	
def sectores(request):
	listado = Sectores.objects.all()

	values = {
		'listado' : listado
	}
	return render_to_response('turnos/sector.html',values,context_instance=RequestContext(request))	
	
def sector_save(request):
	if request.method == 'POST':
		sector = SectoresForm(request.POST)
		if sector.is_valid():
			sector.save()
			
		else:
			values = {
				'sector' : sector,
				'errors'  : sector.errors,
			}
			return render_to_response('turnos/sector_nuevo.html',values,context_instance=RequestContext(request))
	return HttpResponseRedirect(reverse('sector'))
	
def sector_delete(request,id):
	sector = Sectores.objects.get(id=id)
	sector.delete()
	return HttpResponseRedirect(reverse('sector'))
	
def sector_edit(request,id):
	sector = SectoresForm(instance=Sectores.objects.get(id=id))
	if request.method == 'POST':
		form = SectoresForm(request.POST)
		if form.is_valid():
			sector = Sectores.objects.get(id=id)
			sector.descripcion_sector		= form.cleaned_data['descripcion_sector']
			sector.nombre_sector		= form.cleaned_data['nombre_sector']
			sector.save()
			return HttpResponseRedirect(reverse('sector'))
	values = {
		'sector' : sector,
		'id' 	  : id,
	}

	return render_to_response('turnos/sector_edit.html',values,context_instance=RequestContext(request))	



def turno(request): #patty
	listado = Turnos.objects.all()

	values = {
		'listado' : listado
	}
	return render_to_response('turnos/turno.html',values,context_instance=RequestContext(request))

def turno_nuevo(request):
	turno 	= TurnosForm()

	values = {
		'turno':turno,
	}

	return render_to_response('turnos/turno_nuevo.html',values,context_instance=RequestContext(request))

def turno_save(request):
	if request.method == 'POST':
		turno = TurnosForm(request.POST)
		if turno.is_valid():
			turno.save()
			
		else:
			values = {
				'turno' : turno,
				'errors'  : turno.errors,
			}
			return render_to_response('turnos/turno_nuevo.html',values,context_instance=RequestContext(request))
	return HttpResponseRedirect(reverse('turno'))

def turno_edit(request,id):
	turno = TurnosForm(instance=Turnos.objects.get(id=id))
	if request.method == 'POST':
		form = TurnosForm(request.POST)
		if form.is_valid():
			turno = Turnos.objects.get(id=id)
			turno.cliente			= form.cleaned_data['cliente']
			turno.sector			= form.cleaned_data['sector']
			turno.numero			= form.cleaned_data['numero']
			turno.fecha			= form.cleaned_data['fecha']
			turno.save()
			return HttpResponseRedirect(reverse('turno'))
	values = {
		'turno' : turno,
		'id' 	  : id,
	}

	return render_to_response('turnos/turno_edit.html',values,context_instance=RequestContext(request))

def turno_delete(request,id):
	turno = Turnos.objects.get(id=id)
	turno.delete()
	return HttpResponseRedirect(reverse('turno'))
		

def boxAtencion_cambiar_estado(request,id):
	box = BoxAtencion.objects.get(id=id)
	if box.habilitado:
		box.habilitado = False
		box.save()
	else:
		box.habilitado = True 
		box.save()
	return HttpResponseRedirect(reverse('boxAtencion'))

def vista_empleado(request):
	box 	= boxAtencion.objects.get(id=1)
	sectores = box.sectores.all()
	pass


def atender_siguiente(sectores):
	
	for sector in sectores:
		filtro = Turnos.objects.filter(estado='ESPERA',sector=sector)
