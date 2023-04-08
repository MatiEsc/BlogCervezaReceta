from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppRegistro.models import  User, Avatar

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppRegistro.forms import UserRegisterForm, UserEditForm, AvatarFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url = None
    if avatares:
        url= avatares[0].imagen.url
    return render(request, 'inicio.html', {'url': url})

def login_request(request):
    if request.method== "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra= form.cleaned_data.get ("password")

            user = authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)

                return render (request, "inicio.html", {"mensaje": "Bienvenido {usuario}"})

            else:
                return render (request, "inicio.html", {"mensaje": "Error, datos incorrectos"})

        else:
            return render (request, "inicio.html", {"mensaje": "Error, formulario erroneo"})

    form= AuthenticationForm()

    return render (request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username= form.cleaned_data["username"]
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario Creado"})

    else:
        form=UserRegisterForm()

    return render(request, "registro.html", {"form":form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(miFormulario)
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje':'Contraseña incorrecta.'})

            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            avatar_actual = Avatar.objects.filter(user=request.user).first()
            if avatar_actual:
                avatar_actual.imagen = miFormulario.cleaned_data['imagen']
                avatar_actual.save()
            else:
                u = User.objects.get(username=request.user)
                avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
                avatar.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'agregarAvatar.html', {'miFormulario':miFormulario})
