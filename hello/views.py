from django.http import HttpResponse

def index(request):
	return HttpResponse('''Welcome to the Web<br>
<a href="/bot">Bot</a><br>
<a href="/movie">Movie</a><br>
''')
