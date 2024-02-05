from django.http import HttpResponse, JsonResponse
#se importa la libreria models, que tiene los objetos
from .models import Proyecto, Task
from django.shortcuts import get_list_or_404
# Create your views here.

def index(request):
    return HttpResponse("index page")

def hello(request, username):
    # para obtener el parametro impreso en el body
    # se usa HttpResponse('<h2> Hello %s </h2>' % username)
    return HttpResponse('<h2> Hello %s </h2>' % username)

def about(request):
    return HttpResponse('About')

def project(request):
    #   Crea una lista de los objetos, y la guarda en un Json
    project = list(Proyecto.objects.values())
    return JsonResponse(project, safe=False)

def task(request, title):
    #   Obtener datos de un objeto mediante 
    task = Task.objects.get(title=title)    
    return HttpResponse('task: %s' % task.title)
