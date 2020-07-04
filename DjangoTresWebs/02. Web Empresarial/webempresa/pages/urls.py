from django.urls import path
from . import views

urlpatterns = [
    # Paths de blog
    path('<int:page_id>/', views.page, name="page"),
]
