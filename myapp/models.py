from django.db import models

# aqui se crean los modelos especificos
class Proyecto(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " +  self.project.name
    
