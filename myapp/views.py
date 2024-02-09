#   Importaciones
from django.http import HttpResponse
#se importa la libreria models, que tiene los objetos
from .models import Proyecto, Task
from django.shortcuts import render, redirect

#se importa el archivo forms, que almacena todos los datos necesitados ingresados por el usuario en el backend
from .forms import createNewTask, createNewProject

# Create your views here.
def index(request):
    title = "Welcome to django Course"
    prueba = 'con esto sabre la funcion correcta del return'
    return render(request,'index.html',{
        'title': title,
        'prueba': prueba
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
    return render(request, 'projects/project.html', {
        'project': project})

def task(request):
    #   Obtener datos de un objeto mediante 
    #task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request, 'task/task.html', {
        'task': task,
    })

def create_task(request):
    
    #imprime los datos en la consola
    #print(request.GET['title'])
    #print(request.GET['description'])
    
    if request.method == 'GET':
        #   Show interface
        return render(request, 'task/create_task.html', {
            'form': createNewTask()
        })
        
    else:
        #esto crea una nueva tarea en la clase Task, con los parametros ingresados, que son: title, description, y el project 
        Task.objects.create(title=request.POST['title'], descripcion=request.POST['description'], project_id = 3 )
        return redirect('/task/')

#   Crea una nueva funcion, para crear en este caso los proyectos
def create_project(request):


    if request.method == 'GET':

        return render(request, 'projects/create_project.html', {
            'form': createNewProject()
        })

    else:
        Proyecto.objects.create(name=request.POST['name'])
        return redirect('/project/')