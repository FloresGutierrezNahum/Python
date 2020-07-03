# Proyecto 1 - WebPersonal  
https://www.udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/learn/lecture/8627622#questions  

**1. Librerias**  
pip install django==2.0.2  
pip install pylint
pip install pillow

**2. Crear proyecto**  
django-admin startproject webpersonal  
django-admin startapp quickstart   

python manage.py startapp core  
python manage.py startapp portfolio   
  
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

