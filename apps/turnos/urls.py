from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^tipo_cliente/$', views.tipo_cliente, name='tipo_cliente'),
	url(r'^tipo_cliente_nuevo/$', views.tipo_cliente_nuevo, name = 'tipo_cliente_nuevo'),
	url(r'^tipo_cliente_save/$', views.tipo_cliente_save, name = 'tipo_cliente_save'),
	url(r'^tipo_cliente_delete/(?P<id>\d+)/$', views.tipo_cliente_delete, name = 'tipo_cliente_delete'),
	url(r'^tipo_cliente_edit/(?P<id>\d+)/$', views.tipo_cliente_edit, name = 'tipo_cliente_edit'),
	url(r'^cliente/$', views.cliente, name='cliente'),
	url(r'^cliente_nuevo/$', views.cliente_nuevo, name = 'cliente_nuevo'),
	url(r'^cliente_save/$', views.cliente_save, name = 'cliente_save'),
	url(r'^cliente_delete/(?P<id>\d+)/$', views.cliente_delete, name = 'cliente_delete'),
	url(r'^cliente_edit/(?P<id>\d+)/$', views.cliente_edit, name = 'cliente_edit'),
	url(r'^tramite/$', views.tramites, name='tramite'),
	url(r'^tramite_nuevo/$', views.tramite_nuevo, name = 'tramite_nuevo'),
	url(r'^tramite_save/$', views.tramite_save, name = 'tramite_save'),
	url(r'^tramite_delete/(?P<id>\d+)/$', views.tramite_delete, name = 'tramite_delete'),
	url(r'^tramite_edit/(?P<id>\d+)/$', views.tramite_edit, name = 'tramite_edit'),
	url(r'^auto_nuevo/$',views.auto_nuevo,name='auto_nuevo'),
	url(r'^auto_save/$', views.auto_save, name = 'auto_save'),
	url(r'^auto_edit/(?P<id>\d+)/$', views.auto_edit, name = 'auto_edit'),
	url(r'^auto/$', views.auto, name='auto'),
	url(r'^auto_delete/(?P<id>\d+)/$', views.auto_delete, name = 'auto_delete'),
]