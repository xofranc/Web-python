from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index page")
def hola(request, user):
    print(type(user))
    return HttpResponse('<h1>Hello %s</h1>' % user)

def about(request):
    return HttpResponse('About')
