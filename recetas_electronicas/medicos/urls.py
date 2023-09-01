from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name= "home"),
    path('medicos/', medicos, name= "medicos"),
    path('personal/', personal, name= "personal"),
    path('turnos/', turnos, name= "turnos"),
    path('agregar_medico/', add_medico, name="agregar_medico"),
    path('agregar_personal/', add_personal, name="agregar_personal"),
    path('agregar_turno/', add_turno, name="agregar_turno"),
    path('buscar_medico/', buscarmedicos, name="buscar_medico"),
    path('buscar2', buscar2, name="buscar2"),
    path('login', login_request, name='login'),
    path('logout', LogoutView.as_view(template_name="medicos/logout.html"), name='logout'),
    path('registro', registro, name='registro'),
    path('editarPerfil', perfil, name='editarPerfil'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),

]