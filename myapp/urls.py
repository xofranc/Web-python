from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:user>', views.hello),

    #se pueden ingresar variables para que sean vistas en el url del servidor, 
    #se especifica el tipo de dato, que en este caso es str y la variable que en 
    #este caso es username, se puede llenar con cualquier nombre la variable 
    #Ejemplo: 

    path('project/', views.project),

    #Santiago/ o Diego/, pero no se puede dejar vacio, o presentara un error 404, porque este espera algun tipo de parametro

    path('task', views.task),


]
