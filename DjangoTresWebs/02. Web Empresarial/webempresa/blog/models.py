from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name     = models.CharField(max_length=100, verbose_name="Nombre")
    created  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")   #Se agrega al crear
    updated  = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")       #Cambia con cada modificación   

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created'] #Se ordena por fecha de creación (-) :desc

    def __str__(self):
        return self.title

class Post(models.Model):
    title      = models.CharField(max_length=200, verbose_name="Titulo")
    content    = models.TextField(verbose_name="contenido")
    published  = models.DateTimeField(verbose_name="Fecha de publicación", default = timezone.now())
    image      = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author     = 
    categories = 
    created    = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated    = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")   

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created'] #Se ordena por fecha de creación (-) :desc

    def __str__(self):
        return self.title