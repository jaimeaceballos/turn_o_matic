 # -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
# luego de crear los modelos debemos desde la consola
# python manage.py makemigrations
# python manage.py migrate


class TipoCliente(models.Model):
	tipo 		= models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % self.tipo.upper()

class Cliente(models.Model):
	tipo_cliente	= models.ForeignKey('TipoCliente',related_name='de_tipo')
	dni				= models.CharField(max_length=10)
	nombre 			= models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % self.nombre.upper()

class Tramites(models.Model):
	descripcion 	= models.CharField(max_length=50)
	sector 			= models.ForeignKey('Sectores',default="1",related_name="tramite_asociado")

	def __unicode__(self):
		return u'%s' % self.descripcion.upper()


class Sectores(models.Model):
	nombre_sector     	= models.CharField(max_length=50)
	descripcion_sector	= models.CharField(max_length=200)
	codigo 			 	= models.CharField(max_length=2)

	def __unicode__(self):
		return u'%s' % self.nombre_sector.upper()

class BoxAtencion(models.Model):
	nro_box			= models.IntegerField()
	empleado 		= models.CharField(max_length=50)
	habilitado 		= models.BooleanField(default=False)
	sectores 		= models.ManyToManyField(Sectores)

	def __unicode__(self):
		return u'%d - %s' % (self.nro_box,self.empleado)



class Auto(models.Model):
	patente 	= models.CharField(max_length=12)
	marca_modelo = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s - %s' % (self.marca_modelo, self.patente)


class Turnos(models.Model): #patty
	cliente   	= models.ForeignKey(Cliente,null=True)
	sector    	=	models.ForeignKey(Sectores)
	numero	  	= models.IntegerField()
	fecha     	= models.DateTimeField()
	no_cliente 	= models.CharField(max_length=12,null=True,blank=True)
	estado 		= models.CharField(max_length=25)
	atendido_por= models.ForeignKey(BoxAtencion,null=True)
	derivado_a  = models.ForeignKey(Sectores,null=True,related_name='derivado')
	tramite 	= models.ForeignKey(Tramites,null=True)
	
	def __unicode__(self):
		return u'%s' % self.cliente

		
