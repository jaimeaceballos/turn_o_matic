from django.test import TestCase
from models import *
from django.core import serializers

# Create your tests here.

def nuevo_atencion():
	nuevo_atencion 	= TurnosAtencion.objects.latest('id')
	data = serializers.serialize("json", [nuevo_atencion,])
	return data