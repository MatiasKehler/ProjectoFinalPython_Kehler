from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "medicos/home.html")

@login_required
def medicos(request):
    prueba = {'doctor': Medicos.objects.all() }
    return render(request, "medicos/medicos.html", prueba)

@login_required
def personal(request):
    test = {'personas': Personal.objects.all()}
    return render(request, "medicos/personal.html", test)

@login_required
def turnos(request):
    test1 = {'fechas': Turnos.objects.all()}
    return render(request, "medicos/turnos.html", test1)

@login_required
def add_medico(request):
    if request.method == "POST":
        formulario = MedicoForm(request.POST)
        if formulario.is_valid():
            formulario_apellido = formulario.cleaned_data.get('apellido')
            formulario_nombre = formulario.cleaned_data.get('nombre')
            formulario_matricula = formulario.cleaned_data.get('matricula')
            formulario_profesion = formulario.cleaned_data.get('profesion')
            formulario_usuario = formulario.cleaned_data.get('usuario')
            formulario_contraseña = formulario.cleaned_data.get('contraseña')
            formulario_email = formulario.cleaned_data.get('email')
            formulario_sector = formulario.cleaned_data.get('sector')
            final = Medicos(apellido = formulario_apellido, nombre = formulario_nombre, matricula = formulario_matricula,
                            profesion = formulario_profesion, usuario = formulario_usuario, contraseña = formulario_contraseña,
                            email = formulario_email, sector = formulario_sector)
            final.save()
            return render(request, "medicos/home.html")
    else:
        formulario = MedicoForm()

    return render(request, "medicos/agregar_medico.html", {"form": formulario})

@login_required
def add_personal(request):
    if request.method == "POST":
        formulario = PersonalFrom(request.POST)
        if formulario.is_valid():
            formulario_apellido = formulario.cleaned_data.get('apellido')
            formulario_nombre = formulario.cleaned_data.get('nombre')
            formulario_email = formulario.cleaned_data.get('email')
            formulario_sector = formulario.cleaned_data.get('sector')
            final = Personal(apellido = formulario_apellido, nombre = formulario_nombre,
                            email = formulario_email, sector = formulario_sector)
            final.save()
            return render(request, "medicos/home.html")
    else:
        formulario = PersonalFrom()

    return render(request, "medicos/agregar_personal.html", {"form": formulario})

@login_required
def add_turno(request):
    if request.method == "POST":
        formulario = TurnosForm(request.POST)
        if formulario.is_valid():
            formulario_especialidad = formulario.cleaned_data.get('especialidad')
            formulario_turno = formulario.cleaned_data.get('turno')
            final = Turnos(especialidad = formulario_especialidad, turno = formulario_turno)
            final.save()
            return render(request, "medicos/home.html")
    else:
        formulario = TurnosForm()

    return render(request, "medicos/agregar_turno.html", {"form": formulario})

@login_required
def buscarmedicos(request):
    return render(request, "medicos/buscar_medico.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        busqueda = request.GET['buscar']
        apellido = Medicos.objects.filter(apellido__icontains = busqueda)
        nombre = Medicos.objects.filter(nombre__icontains= busqueda)
        if nombre:
            context = {'doctor': nombre}
        if apellido:
            context = {'doctor': apellido}
        return render(request, "medicos/medicos.html", context)
    return HttpResponse("Ingreso un dato no valido.")

def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "medicos/home.html", {'mensaje': f'¡Bienvenido!{usuario}'})
            else:
                return render(request, "medicos/login.html", {'form': formulario, 'mensaje': f'Los datos cargados son inconrrectos.'})
        else:
            return render(request, "medicos/login.html", {'form': formulario, 'mensaje': f'Los datos cargados son inconrrectos.'})

    formulario = AuthenticationForm() 
    return render(request, "medicos/login.html", {'form': formulario})


def registro(request):
    if request.method == "POST":
        formulario = RegistroFrom(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            formulario.save()
            return render(request, "medicos/home.html")
    else:
        formulario = RegistroFrom()
    return render(request, "medicos/registro.html", {"form":formulario})

@login_required
def perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "Medicos/home.html")
        else:
            return render(request, "Medicos/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "Medicos/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarviejo = Avatar.objects.filter(user=u)
            if len(avatarviejo) > 0:
                avatarviejo[0].delete()
                
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "Medicos/home.html")
    else:
        form = AvatarForm()
    return render(request, "Medicos/agregarAvatar.html", {'form': form})