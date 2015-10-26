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

	def __unicode__(self):
		return u'%s' % self.descripcion.upper()


class Auto(models.Model):
	patente 	= models.CharField(max_length=12)
	marca_modelo = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s - %s' % (self.marca_modelo, self.patente)

