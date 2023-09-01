from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('nuestros_servicios/', nuestros_servicios, name="nuestros_servicios"),
]