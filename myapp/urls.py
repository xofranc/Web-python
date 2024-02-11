from django.urls import path
from . import views
    #se pueden ingresar variables para que sean vistas en el url del servidor,
    #se especifica el tipo de dato, que en este caso es str y la variable que en
    #este caso es username, se puede llenar con cualquier nombre la variable
    #Ejemplo:

    #Santiago/ o Diego/, pero no se puede dejar vacio, o presentara un error 404, porque este espera algun tipo de parametro
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('details/<int:id>', views.projectDetail, name='project_detail'),
    path('task/', views.task, name='task'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')


]
