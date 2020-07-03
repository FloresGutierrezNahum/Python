from django.urls import path
from . import views

urlpatterns = [
    # Paths de blog
    path('', views.blog, name ="blog"),
]
