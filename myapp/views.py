#   Importaciones
from django.http import HttpResponse
#se importa la libreria models, que tiene los objetos
from .models import Proyecto, Task
from django.shortcuts import render
# Create your views here.


def index(request):
    title = "Welcome to django Course"
    return render(request,'index.html',{
        'title': title
    })

def about(request):
    username = 'Santiago'
    return render(request, 'about.html',{
        'username': username
    }) 

def hello(request, username):
    # para obtener el parametro impreso en el body
    # se usa HttpResponse('<h2> Hello %s </h2>' % username)
    return render(request, 'hello.html', {'username': username})

def project(request):
    #   Crea una lista de los objetos, y la guarda en un Json
    #   project = list(Proyecto.objects.values())
    project = Proyecto.objects.all()
    return render(request, 'project.html', {
        'project': project})

def task(request):
    #   Obtener datos de un objeto mediante 
    #task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request, 'task.html', {
        'task': task,
    })
