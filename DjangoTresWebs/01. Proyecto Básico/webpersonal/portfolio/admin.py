from django.contrib import admin
from .models import Project # . hace referencia al mismo directorio

# Register your models here.
admin.site.register(Project)