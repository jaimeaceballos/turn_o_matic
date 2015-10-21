from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^tipo_cliente/$', views.tipo_cliente, name='tipo_cliente'),
	url(r'^tipo_cliente_nuevo/$', views.tipo_cliente_nuevo, name = 'tipo_cliente_nuevo'),
	url(r'^tipo_cliente_save/$', views.tipo_cliente_save, name = 'tipo_cliente_save'),
	url(r'^tipo_cliente_delete/(?P<id>\d+)/$', views.tipo_cliente_delete, name = 'tipo_cliente_delete'),
	url(r'^tipo_cliente_edit/(?P<id>\d+)/$', views.tipo_cliente_edit, name = 'tipo_cliente_edit'),

]