#Se definen las vistas de una app
#La vista hace referencia a la lógica que se ejecuta cuando se hace una petición a la web
#Se crea una vista para procesar la petición a la raiz del sitio web

from django.shortcuts import render, HttpResponse

html_base = """
<h1> Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>

"""

# Create your views here.
def home (request):
   return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")