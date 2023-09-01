from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MedicoForm(forms.Form):
    apellido = forms.CharField(max_length=15, required=True)
    nombre = forms.CharField(max_length=15, required=True)
    matricula = forms.IntegerField(required=True)
    profesion = forms.CharField(max_length=15, required=True)
    usuario = forms.CharField(max_length=15, required=True)
    contraseña = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=False)
    sector = forms.CharField(max_length=15, required=True)

class PersonalFrom(forms.Form):
    apellido = forms.CharField(max_length=15, required=True)
    nombre = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=False)
    sector = forms.CharField(max_length=15, required=True)

class TurnosForm(forms.Form):
    especialidad = forms.CharField(max_length=15, required=True)
    turno = forms.DateField(required=True)

class RegistroFrom(UserCreationForm):
    email = forms.EmailField(label="Email del usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email del usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=25, required=False)
    last_name = forms.CharField(label="Apellido", max_length=25, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
