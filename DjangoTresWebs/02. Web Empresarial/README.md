# Proyecto 2 - WebEmpresa  
https://www.udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/learn/lecture/9616016#questions

**1. Librerias**  
pip install django==2.0.2  
pip install pylint
pip install pillow

**2. Crear proyecto**  
django-admin startproject webempresa  
django-admin startapp quickstart   

python manage.py startapp core     
  
python manage.py makemigrations portfolio **(verificar cambios en una app)**  
python manage.py migrate portfolio **(aplicar cambios de una app)**  
    

**3. Crear templates**  
Crear una carpeta templates y dentro de la carpeta se crea otra carpeta con el nombre de la app (core)  


**x. Configurar runserver para correr recursos estáticos**  
Crear una carpeta **static** en la la app  
crear una carpeta con el nombre de la app **(core)** dentro de static  
copiar en la carpeta todos los recursos del front  

**x. Migrations**  
python manage.py makemigrations  
python manage.py migrate  

**x. Creación de SuperUsuario**  
python manage.py createsuperuser 

**x. Correr servidor**  
python manage.py runserver

**x. Extensión de vscode**  
Django template  
  
  
  
**I. Info**  
- ORM: Modelo Objeto Relacional, si se siguen las pautas de Django se pueden trabajar con objetos 
mapeados en la base de datos, de manera que al crear instancias de una clase específica estas quedarán guardadas 
como registros de forma automática y cuando las recuperemos y modifiquemos, los valores quedarán guardados en la 
base de datos (**en django estos objetos persistentes son llamados modelos**).   
  
- Para usar los modelos creados importar el modelo en **admin.py** de la aplicación  
  
- Al traducir una app se extiende la aplicación en "INSTALLED_APPS" **services ->  services.apps.ServicesConfig**  

**I. Considerar para las apps (social)**  
**a)** crear modelo **(models.py)**   
**b)** verbose_name para la app **(apps.py)**   
**c)** registrar app **(settings.py [social.apps.SocialConfig])**   
**d)** makemigrations social, migrate social  
**e)** crear adiministrador de prueba **social..(admin.py)**   
  

**E1. Mover un template de core -> app**  
- blog: Crear carpeta **templates\blog**  y mover el .html del core a la carpeta  
- Modificar las URLs: Se corta la url de blog que está en core a las **urls.py (se crea)** en blog | al 
copiar se tiene que dejar el path en la raiz **[path('', views.blog, name ="blog")]**  
- Agregar el path de blog a las URLs de proyecto **path('blog/', include('blog.urls'))**  

**E2. Dinamizar el template**   
- blog: en **views.py** importar los post **(from .models import Post)**, se obtienen 
todos los objetos **[posts = Post.objects.all()]** se pasa una lista con los datos obtenidos [return render(request, "blog/blog.html",**{'posts':posts}**)]
- blog.html: se usa un template tag for y se hace una llamada a la lista creada **{% for post in posts %} ...   {% endfor %}**  
- blog.html: cambiar las partes estáticas por los datos que están en la lista  **{{post.published}}**, para las imagenes usar **"{{post.image.url}}"**  
  
## Importante
- Video 43 min 10:30 -> Uso de relaciones para obtener datos  - aprovecha la bidireccionalidad de las relaciones  

