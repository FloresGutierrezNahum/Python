# Create your models here.

from django.db import models

#Clases enlazadas a la base de datos

#Se crea una tabla
class Service(models.Model):
    title    = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="SubTitulo")
    content  = models.TextField(verbose_name="Contenido")
    image    = models.ImageField(verbose_name="Imagen")
    created  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")   #Se agrega al crear
    updated  = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")       #Cambia con cada modificación   

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created'] #Se ordena por fecha de creación (-) :desc

    def __str__(self):
        return self.title

