# Create your models here.

from django.db import models


#Clases enlazadas a la base de datos

#Se crea un tabla
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)   #Se agrega al crear
    updated = models.DateTimeField(auto_now=True)       #Cambia con cada modificación

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created'] #Se ordena por fecha de creación (-) :desc