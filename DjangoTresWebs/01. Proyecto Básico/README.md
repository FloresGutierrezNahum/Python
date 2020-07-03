# Proyecto 1 - WebPersonal  
https://www.udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/learn/lecture/8627622#questions  

**1. Librerias**  
pip install django==2.0.2  
pip install pylint

**2. Crear proyecto**  
django-admin startproject webpersonal  
django-admin startapp quickstart   

python manage.py startapp core  

**3. Crear templates**  
Crear una carpeta templates, dentro de la carpeta se crea otra carpeta con el nombre de la app (core)  

**x. Migrations**  
python manage.py makemigrations  
python manage.py migrate  

**x. Creación de SuperUsuario**  
python manage.py createsuperuser 

**x. Correr servidor**  
python manage.py runserver
