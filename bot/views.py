from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
	context = RequestContext(request)
    # Optional Variable to pass value to web html
	context_dict = {'boldmessage' : "This is value from views"}
	return render_to_response('hello/bot.html', context)
