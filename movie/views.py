from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage' : "This is value from views"}
	return render_to_response('hello/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)
	return render_to_response('hello/homepage.html', context)

"""	return HttpResponse('''Nested URL <br>
	This page should contain detail about Movie Database
	<br>
	<a href='/movie/'>Movie</a>
	 ''')
"""
