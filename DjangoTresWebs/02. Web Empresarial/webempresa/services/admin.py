from django.contrib import admin
from .models import Service

# Register your models here

#Función para mostrar las fechas de modificación y subida
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #Tupla con los datos de solo lectura

#admin.site.register(Project)

#Se extiende el reistro
admin.site.register(Service, ServiceAdmin)
