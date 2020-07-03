from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

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
    published  = models.DateTimeField(verbose_name="Fecha de publicación", default = now)
    image      = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author     = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = "Categorias")
    created    = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated    = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")   

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created'] #Se ordena por fecha de creación (-) :desc

    def __str__(self):
        return self.title