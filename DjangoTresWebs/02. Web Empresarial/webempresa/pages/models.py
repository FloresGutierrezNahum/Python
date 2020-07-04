from django.db import models

# Create your models here.
class Page(models.Model):
    title    = models.CharField(verbose_name = "Red Social", max_length=100)
    content  = models.TextField(verbose_name = "contenido")
    created  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")   #Se agrega al crear
    updated  = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")       #Cambia con cada modificación   

    class Meta:         
        #Subclase con los metadatos
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['-title'] #Se ordena por fecha de creación (-) :desc

    def __str__(self):
        return self.title