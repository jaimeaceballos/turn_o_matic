from django.shortcuts import render, render_to_response
from django.template.context import RequestContext


# Create your views here.


def home (request):
		
	values={}
	return render_to_response('index.html',values,context_instance = RequestContext(request))