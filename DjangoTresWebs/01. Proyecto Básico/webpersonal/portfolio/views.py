from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() #Devuelve todos los objetos que tiene el modelo de project
    #return render(request, "portfolio/portfolio.html")
    return render(request, "portfolio/portfolio.html", {'projects':projects})