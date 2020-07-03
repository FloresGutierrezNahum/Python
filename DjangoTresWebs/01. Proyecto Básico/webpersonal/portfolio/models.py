# Create your models here.

from django.db import models


#Clases enlazadas a la base de datos

#Se crea un tabla
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") #Guarda las imagenes media en el directorio projects
    link = models.URLField(verbose_name="Dirección Web",null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")   #Se agrega al crear
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")       #Cambia con cada modificación
    

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created'] #Se ordena por fecha de creación (-) :desc

    def __str__(self):
        return self.title