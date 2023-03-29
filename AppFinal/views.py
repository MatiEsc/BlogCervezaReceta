from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppFinal.models import AmericanasAle, AlemanasChecasAustriacasAle, BelgasFrancesasAle, BritanicasAle, InternacionalesAle, AmericanasLager, AlemanasChecasAustriacasLager, InternacionalesLager, Otras, Avatar
from AppFinal.forms import AmericanasAleFormulario, AlemanasChecasAustriacasAleFormulario, BelgasFrancesasAleFormulario, BritanicasAleFormulario, InternacionalesAleFormulario, AmericanasLagerFormulario, AlemanasChecasAustriacasLagerFormulario, InternacionalesLagerFormulario, OtrasFormulario, AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFinal.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import make_password


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def americanasAle(request):
    if request.method == 'POST':
        miFormulario = AmericanasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            americanasAle = AmericanasAle(
                                          nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            americanasAle.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AmericanasAleFormulario()
    
    return render(request, 'americanasAle.html', {'miFormulario':miFormulario})



def alemanasChecasAustriacasAle(request):
    if request.method == 'POST':
        miFormulario = AlemanasChecasAustriacasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            alemanasChecasAustriacasAle = AlemanasChecasAustriacasAle(
                                                                    nombre=informacion['nombre'],
                                                                    maltas=informacion['maltas'],
                                                                    lupulo=informacion["lupulo"],
                                                                    levadura=informacion["levadura"],
                                                                    adicionales=informacion["adicionales"],
                                                                    procesoDeCoccion=informacion['proceso_De_Coccion'],
                                                                    emailDeContacto=informacion["email_De_Contacto"],
                                                                    fechaDePublicacion=informacion["fecha_De_Publicacion"])

            alemanasChecasAustriacasAle.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AlemanasChecasAustriacasAleFormulario()
    
    return render(request, 'alemanasChecasAustriacasAle.html', {'miFormulario':miFormulario})


def belgasFrancesasAle(request):
    if request.method == 'POST':
        miFormulario = BelgasFrancesasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            belgasFrancesasAle = BelgasFrancesasAle(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            belgasFrancesasAle.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = BelgasFrancesasAleFormulario()
    
    return render(request, 'belgasFrancesasAle.html', {'miFormulario':miFormulario})


def britanicasAle(request):
    if request.method == 'POST':
        miFormulario = BritanicasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            britanicasAle = BritanicasAle(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            britanicasAle.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = BritanicasAleFormulario()
    
    return render(request, 'britanicasAle.html', {'miFormulario':miFormulario})


def internacionalesAle(request):
    if request.method == 'POST':
        miFormulario = InternacionalesAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            internacionalesAle = InternacionalesAle(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            internacionalesAle.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = InternacionalesAleFormulario()
    
    return render(request, 'internacionalesAle.html', {'miFormulario':miFormulario})


def americanasLager(request):
    if request.method == 'POST':
        miFormulario = AmericanasLagerFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            americanasLager = AmericanasLager(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            americanasLager.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AmericanasLagerFormulario()
    
    return render(request, 'americanasLager.html', {'miFormulario':miFormulario})



def alemanasChecasAustriacasLager(request):
    if request.method == 'POST':
        miFormulario = AlemanasChecasAustriacasLagerFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            alemanasChecasAustriacasLager = AlemanasChecasAustriacasLager(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            alemanasChecasAustriacasLager.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AlemanasChecasAustriacasLagerFormulario()
    
    return render(request, 'alemanasChecasAustriacasLager.html', {'miFormulario':miFormulario})

def internacionalesLager(request):
    if request.method == 'POST':
        miFormulario = InternacionalesLagerFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            internacionalesLager = InternacionalesLager(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            internacionalesLager.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = InternacionalesLagerFormulario()
    
    return render(request, 'internacionalesLager.html', {'miFormulario':miFormulario})

def otras(request):
    if request.method == 'POST':
        miFormulario = OtrasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            otras = Otras(nombre=informacion['nombre'],
                                          maltas=informacion['maltas'],
                                          lupulo=informacion["lupulo"],
                                          levadura=informacion["levadura"],
                                          adicionales=informacion["adicionales"],
                                          procesoDeCoccion=informacion['proceso_De_Coccion'],
                                          emailDeContacto=informacion["email_De_Contacto"],
                                          fechaDePublicacion=informacion["fecha_De_Publicacion"])

            otras.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = OtrasFormulario()
    
    return render(request, 'otras.html', {'miFormulario':miFormulario})

def cargarReceta(request):
    return render(request, "cargarReceta.html")

def mostrarReceta(request):
    return render(request, "mostrarReceta.html")

def leerAmericanasAle(request):
    americanasAle= AmericanasAle.objects.all()
    contexto = {"americanasAle": americanasAle}
    return render (request, "leerAmericanasAle.html", contexto)

def leerAlemanasChecasAustriacasAle(request):
    alemanasChecasAustriacasAle= AlemanasChecasAustriacasAle.objects.all()
    contexto = {"alemanasChecasAustriacasAle": alemanasChecasAustriacasAle}
    return render (request, "leerAlemanasChecasAustriacasAle.html", contexto)

def leerBelgasFrancesasAle(request):
    belgasFrancesasAle= BelgasFrancesasAle.objects.all()
    contexto = {"belgasFrancesasAle": belgasFrancesasAle}
    return render (request, "leerBelgasFrancesasAle.html", contexto)

def leerBritanicasAle(request):
    britanicasAle= BritanicasAle.objects.all()
    contexto = {"britanicasAle": britanicasAle}
    return render (request, "leerBritanicasAle.html", contexto)

def leerInternacionalesAle(request):
    internacionalesAle= internacionalesAle.objects.all()
    contexto = {"internacionalesAle": internacionalesAle}
    return render (request, "leerInternacionalesAle.html", contexto)

def leerAmericanasLager(request):
    americanasLager= AmericanasLager.objects.all()
    contexto = {"americanasLager": americanasLager}
    return render (request, "leerAmericanasLager.html", contexto)

def leerAlemanasChecasAustriacasLager(request):
    alemanasChecasAustriacasLager= AlemanasChecasAustriacasLager.objects.all()
    contexto = {"alemanasChecasAustriacasLager": alemanasChecasAustriacasLager}
    return render (request, "leerAlemanasChecasAustriacasLager.html", contexto)

def leerInternacionalesLager(request):
    internacionalesLager= InternacionalesLager.objects.all()
    contexto = {"internacionalesLager": internacionalesLager}
    return render (request, "leerInternacionalesLager.html", contexto)

def leerOtras(request):
    otras= otras.objects.all()
    contexto = {"otras": otras}
    return render (request, "leerOtras.html", contexto)


def editarAmericanasAle(request, americanasAle_nombre):
    americanasAle= AmericanasAle.objects.get(nombre=americanasAle_nombre)

    if request.method == "POST":
        miFormulario= AmericanasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            americanasAle.nombre= informacion ["nombre"]
            americanasAle.maltas= informacion ["maltas"]
            americanasAle.lupulo= informacion ["lupulo"]
            americanasAle.levadura= informacion ["levadura"]
            americanasAle.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            americanasAle.emailDeContacto= informacion ["email_De_Contacto"]
            americanasAle.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            americanasAle.imagen= informacion ["imagen"]


            americanasAle.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= AmericanasAleFormulario(initial={"nombre": americanasAle.nombre,
                                                       "maltas": americanasAle.maltas,
                                                        "lupulo": americanasAle.lupulo,
                                                        "levadura": americanasAle.levadura,
                                                        "procesoDeCoccion":americanasAle.procesoDeCoccion,
                                                        "emailDeContacto": americanasAle.emailDeContacto,
                                                        "fechaDePublicacion": americanasAle.fechaDePublicacion,
                                                        "imagen": americanasAle.imagen})
            
        return render (request, "editarAmericanasAle.html",
                            {"miFormulario":miFormulario, "americanasAle_nombre":americanasAle_nombre})

def editarAlemanasChecasAustriacasAle(request, alemanasChecasAustriacasAle_nombre):
    alemanasChecasAustriacasAle= AlemanasChecasAustriacasAle.objects.get(nombre=alemanasChecasAustriacasAle_nombre)

    if request.method == "POST":
        miFormulario= AlemanasChecasAustriacasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            alemanasChecasAustriacasAle.nombre= informacion ["nombre"]
            alemanasChecasAustriacasAle.maltas= informacion ["maltas"]
            alemanasChecasAustriacasAle.lupulo= informacion ["lupulo"]
            alemanasChecasAustriacasAle.levadura= informacion ["levadura"]
            alemanasChecasAustriacasAle.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            alemanasChecasAustriacasAle.emailDeContacto= informacion ["email_De_Contacto"]
            alemanasChecasAustriacasAle.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            alemanasChecasAustriacasAle.imagen= informacion ["imagen"]


            alemanasChecasAustriacasAle.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= AlemanasChecasAustriacasAleFormulario(initial={"nombre": alemanasChecasAustriacasAle.nombre,
                                                       "maltas": alemanasChecasAustriacasAle.maltas,
                                                        "lupulo": alemanasChecasAustriacasAle.lupulo,
                                                        "levadura": alemanasChecasAustriacasAle.levadura,
                                                        "procesoDeCoccion":alemanasChecasAustriacasAle.procesoDeCoccion,
                                                        "emailDeContacto": alemanasChecasAustriacasAle.emailDeContacto,
                                                        "fechaDePublicacion": alemanasChecasAustriacasAle.fechaDePublicacion,
                                                        "imagen": alemanasChecasAustriacasAle.imagen})
            
        return render (request, "editarAlemanasChecasAustriacasAle.html",
                            {"miFormulario":miFormulario, "alemanasChecasAustriacasAle_nombre":alemanasChecasAustriacasAle_nombre})
    
def editarBelgasFrancesasAle(request, belgasFrancesasAle_nombre):
    belgasFrancesasAle= BelgasFrancesasAle.objects.get(nombre=belgasFrancesasAle_nombre)

    if request.method == "POST":
        miFormulario= BelgasFrancesasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            belgasFrancesasAle.nombre= informacion ["nombre"]
            belgasFrancesasAle.maltas= informacion ["maltas"]
            belgasFrancesasAle.lupulo= informacion ["lupulo"]
            belgasFrancesasAle.levadura= informacion ["levadura"]
            belgasFrancesasAle.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            belgasFrancesasAle.emailDeContacto= informacion ["email_De_Contacto"]
            belgasFrancesasAle.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            belgasFrancesasAle.imagen= informacion ["imagen"]


            belgasFrancesasAle.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= BelgasFrancesasAleFormulario(initial={"nombre": belgasFrancesasAle.nombre,
                                                       "maltas": belgasFrancesasAle.maltas,
                                                        "lupulo": belgasFrancesasAle.lupulo,
                                                        "levadura": belgasFrancesasAle.levadura,
                                                        "procesoDeCoccion":belgasFrancesasAle.procesoDeCoccion,
                                                        "emailDeContacto": belgasFrancesasAle.emailDeContacto,
                                                        "fechaDePublicacion": belgasFrancesasAle.fechaDePublicacion,
                                                        "imagen": belgasFrancesasAle.imagen})
            
        return render (request, "editarBelgasFrancesasAle.html",
                            {"miFormulario":miFormulario, "belgasFrancesasAle_nombre":belgasFrancesasAle_nombre})

def editarBritanicasAle(request, britanicasAle_nombre):
    britanicasAle= BritanicasAle.objects.get(nombre=britanicasAle_nombre)

    if request.method == "POST":
        miFormulario= BritanicasAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            britanicasAle.nombre= informacion ["nombre"]
            britanicasAle.maltas= informacion ["maltas"]
            britanicasAle.lupulo= informacion ["lupulo"]
            britanicasAle.levadura= informacion ["levadura"]
            britanicasAle.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            britanicasAle.emailDeContacto= informacion ["email_De_Contacto"]
            britanicasAle.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            britanicasAle.imagen= informacion ["imagen"]


            britanicasAle.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= BritanicasAleFormulario(initial={"nombre": britanicasAle.nombre,
                                                       "maltas": britanicasAle.maltas,
                                                        "lupulo": britanicasAle.lupulo,
                                                        "levadura": britanicasAle.levadura,
                                                        "procesoDeCoccion":britanicasAle.procesoDeCoccion,
                                                        "emailDeContacto": britanicasAle.emailDeContacto,
                                                        "fechaDePublicacion": britanicasAle.fechaDePublicacion,
                                                        "imagen": britanicasAle.imagen})
            
        return render (request, "editarBritanicasAle.html",
                            {"miFormulario":miFormulario, "britanicasAle_nombre":britanicasAle_nombre})


def editarInternacionalesAle(request, internacionalesAle_nombre):
    internacionalesAle= InternacionalesAle.objects.get(nombre=internacionalesAle_nombre)

    if request.method == "POST":
        miFormulario= InternacionalesAleFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            internacionalesAle.nombre= informacion ["nombre"]
            internacionalesAle.maltas= informacion ["maltas"]
            internacionalesAle.lupulo= informacion ["lupulo"]
            internacionalesAle.levadura= informacion ["levadura"]
            internacionalesAle.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            internacionalesAle.emailDeContacto= informacion ["email_De_Contacto"]
            internacionalesAle.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            internacionalesAle.imagen= informacion ["imagen"]


            internacionalesAle.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= InternacionalesAleFormulario(initial={"nombre": internacionalesAle.nombre,
                                                       "maltas": internacionalesAle.maltas,
                                                        "lupulo": internacionalesAle.lupulo,
                                                        "levadura": internacionalesAle.levadura,
                                                        "procesoDeCoccion":internacionalesAle.procesoDeCoccion,
                                                        "emailDeContacto": internacionalesAle.emailDeContacto,
                                                        "fechaDePublicacion": internacionalesAle.fechaDePublicacion,
                                                        "imagen": internacionalesAle.imagen})
            
        return render (request, "editarInternacionalesAle.html",
                            {"miFormulario":miFormulario, "internacionalesAle_nombre":internacionalesAle_nombre})


def editarAmericanasLager(request, americanasLager_nombre):
    americanasLager= AmericanasLager.objects.get(nombre=americanasLager_nombre)

    if request.method == "POST":
        miFormulario= AmericanasLagerFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            americanasLager.nombre= informacion ["nombre"]
            americanasLager.maltas= informacion ["maltas"]
            americanasLager.lupulo= informacion ["lupulo"]
            americanasLager.levadura= informacion ["levadura"]
            americanasLager.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            americanasLager.emailDeContacto= informacion ["email_De_Contacto"]
            americanasLager.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            americanasLager.imagen= informacion ["imagen"]


            americanasLager.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= AmericanasLagerFormulario(initial={"nombre": americanasLager.nombre,
                                                       "maltas": americanasLager.maltas,
                                                        "lupulo": americanasLager.lupulo,
                                                        "levadura": americanasLager.levadura,
                                                        "procesoDeCoccion":americanasLager.procesoDeCoccion,
                                                        "emailDeContacto": americanasLager.emailDeContacto,
                                                        "fechaDePublicacion": americanasLager.fechaDePublicacion,
                                                        "imagen": americanasLager.imagen})
            
        return render (request, "editarAmericanasLager.html",
                            {"miFormulario":miFormulario, "americanasLager_nombre":americanasLager_nombre})


def editarAlemanasChecasAustriacasLager(request, alemanasChecasAustriacasLager_nombre):
    alemanasChecasAustriacasLager= AlemanasChecasAustriacasLager.objects.get(nombre=alemanasChecasAustriacasLager_nombre)

    if request.method == "POST":
        miFormulario= AlemanasChecasAustriacasLagerFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            alemanasChecasAustriacasLager.nombre= informacion ["nombre"]
            alemanasChecasAustriacasLager.maltas= informacion ["maltas"]
            alemanasChecasAustriacasLager.lupulo= informacion ["lupulo"]
            alemanasChecasAustriacasLager.levadura= informacion ["levadura"]
            alemanasChecasAustriacasLager.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            alemanasChecasAustriacasLager.emailDeContacto= informacion ["email_De_Contacto"]
            alemanasChecasAustriacasLager.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            alemanasChecasAustriacasLager.imagen= informacion ["imagen"]


            alemanasChecasAustriacasLager.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= AlemanasChecasAustriacasLagerFormulario(initial={"nombre": alemanasChecasAustriacasLager.nombre,
                                                       "maltas": alemanasChecasAustriacasLager.maltas,
                                                        "lupulo": alemanasChecasAustriacasLager.lupulo,
                                                        "levadura": alemanasChecasAustriacasLager.levadura,
                                                        "procesoDeCoccion":alemanasChecasAustriacasLager.procesoDeCoccion,
                                                        "emailDeContacto": alemanasChecasAustriacasLager.emailDeContacto,
                                                        "fechaDePublicacion": alemanasChecasAustriacasLager.fechaDePublicacion,
                                                        "imagen": alemanasChecasAustriacasLager.imagen})
            
        return render (request, "editarAlemanasChecasAustriacasLager.html",
                            {"miFormulario":miFormulario, "alemanasChecasAustriacasLager_nombre":alemanasChecasAustriacasLager_nombre})


def editarInternacionalesLager(request, internacionalesLager_nombre):
    internacionalesLager= InternacionalesLager.objects.get(nombre=internacionalesLager_nombre)

    if request.method == "POST":
        miFormulario= InternacionalesLagerFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            internacionalesLager.nombre= informacion ["nombre"]
            internacionalesLager.maltas= informacion ["maltas"]
            internacionalesLager.lupulo= informacion ["lupulo"]
            internacionalesLager.levadura= informacion ["levadura"]
            internacionalesLager.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            internacionalesLager.emailDeContacto= informacion ["email_De_Contacto"]
            internacionalesLager.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            internacionalesLager.imagen= informacion ["imagen"]


            internacionalesLager.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= InternacionalesAleFormulario(initial={"nombre": internacionalesLager.nombre,
                                                       "maltas": internacionalesLager.maltas,
                                                        "lupulo": internacionalesLager.lupulo,
                                                        "levadura": internacionalesLager.levadura,
                                                        "procesoDeCoccion":internacionalesLager.procesoDeCoccion,
                                                        "emailDeContacto": internacionalesLager.emailDeContacto,
                                                        "fechaDePublicacion": internacionalesLager.fechaDePublicacion,
                                                        "imagen": internacionalesLager.imagen})
            
        return render (request, "editarInternacionalesLager.html",
                            {"miFormulario":miFormulario, "internacionalesLager_nombre":internacionalesLager_nombre})


def editarOtras(request, otras_nombre):
    otras= Otras.objects.get(nombre=otras_nombre)

    if request.method == "POST":
        miFormulario= OtrasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data

            
            otras.nombre= informacion ["nombre"]
            otras.maltas= informacion ["maltas"]
            otras.lupulo= informacion ["lupulo"]
            otras.levadura= informacion ["levadura"]
            otras.procesoDeCoccion= informacion ["proceso_De_Coccion"]
            otras.emailDeContacto= informacion ["email_De_Contacto"]
            otras.fechaDePublicacion= informacion ["fecha_De_Publicacion"]
            otras.imagen= informacion ["imagen"]


            otras.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= InternacionalesAleFormulario(initial={"nombre": otras.nombre,
                                                       "maltas": otras.maltas,
                                                        "lupulo": otras.lupulo,
                                                        "levadura": otras.levadura,
                                                        "procesoDeCoccion": otras.procesoDeCoccion,
                                                        "emailDeContacto": otras.emailDeContacto,
                                                        "fechaDePublicacion": otras.fechaDePublicacion,
                                                        "imagen": otras.imagen})
            
        return render (request, "editarOtras.html",
                            {"miFormulario":miFormulario, "otras_nombre":otras_nombre})

def eliminarAmericanasAle(request, americanasAle_nombre):
    americanasAle= AmericanasAle.objects.get(nombre=americanasAle_nombre)
    americanasAle.delete()

    americanasAle=AmericanasAle.objects.all()
    contexto = {"americanasAle": americanasAle}
    return render (request, "leerAmericanasAle.html", contexto)

def eliminarAlemanasChecasAustriacasAle(request, alemanasChecasAustriacasAle_nombre):
    alemanasChecasAustriacasAle= AlemanasChecasAustriacasAle.objects.get(nombre=alemanasChecasAustriacasAle_nombre)
    alemanasChecasAustriacasAle.delete()

    alemanasChecasAustriacasAle=AlemanasChecasAustriacasAle.objects.all()
    contexto = {"alemanasChecasAustriacasAle": alemanasChecasAustriacasAle}
    return render (request, "leerAlemanasChecasAustriacasAle.html", contexto)

def eliminarBelgasFrancesasAle(request, belgasFrancesasAle_nombre):
    belgasFrancesasAle= BelgasFrancesasAle.objects.get(nombre=belgasFrancesasAle_nombre)
    belgasFrancesasAle.delete()

    belgasFrancesasAle=BelgasFrancesasAle.objects.all()
    contexto = {"belgasFrancesasAle": belgasFrancesasAle}
    return render (request, "leerBelgasFrancesasAle.html", contexto)

def eliminarBritanicasAle(request, britanicasAle_nombre):
    britanicasAle= BritanicasAle.objects.get(nombre=britanicasAle_nombre)
    britanicasAle.delete()

    britanicasAle=BritanicasAle.objects.all()
    contexto = {"britanicasAle": britanicasAle}
    return render (request, "leerBritanicasAle.html", contexto)

def eliminarInternacionalesAle(request, internacionalesAle_nombre):
    internacionalesAle= InternacionalesAle.objects.get(nombre=internacionalesAle_nombre)
    internacionalesAle.delete()

    internacionalesAle=InternacionalesAle.objects.all()
    contexto = {"internacionalesAle": internacionalesAle}
    return render (request, "leerInternacionalesAle.html", contexto)

def eliminarAmericanasLager(request, americanasLager_nombre):
    americanasLager= AmericanasLager.objects.get(nombre=americanasLager_nombre)
    americanasLager.delete()

    americanasLager=AmericanasLager.objects.all()
    contexto = {"americanasLager": americanasLager}
    return render (request, "leerAmericanasLager.html", contexto)

def eliminarAlemanasChecasAustriacasLager(request, alemanasChecasAustriacasLager_nombre):
    alemanasChecasAustriacasLager= AlemanasChecasAustriacasLager.objects.get(nombre=alemanasChecasAustriacasLager_nombre)
    alemanasChecasAustriacasLager.delete()

    alemanasChecasAustriacasLager=AlemanasChecasAustriacasLager.objects.all()
    contexto = {"alemanasChecasAustriacasLager": alemanasChecasAustriacasLager}
    return render (request, "leerAlemanasChecasAustriacasLager.html", contexto)

def eliminarInternacionalesLager(request, internacionalesLager_nombre):
    internacionalesLager= InternacionalesLager.objects.get(nombre=internacionalesLager_nombre)
    internacionalesLager.delete()

    internacionalesLager=InternacionalesLager.objects.all()
    contexto = {"internacionalesLager": internacionalesLager}
    return render (request, "leerInternacionalesLager.html", contexto)

def eliminarOtras(request, otras_nombre):
    otras= Otras.objects.get(nombre=otras_nombre)
    otras.delete()

    otras=Otras.objects.all()
    contexto = {"otras": otras}
    return render (request, "leerOtras.html", contexto)











class AmericanasAleList(ListView):
    model= AmericanasAle
    template_name="americanasAle_list.html"

class AmericanasAleDetalle(DetailView):
    model= AmericanasAle
    template_name="americanasAle_detalle.html"

class AmericanasAleCreacion(CreateView):
    model= AmericanasAle
    template_name="americanasAle_form.html"
    success_url= reverse_lazy("AppFinal:list")
    fields=["nombre", "maltas", "lupulo", "levadura", "adicionales", "procesoDeCoccion", "emailDeContacto", "fechaDePublicacion", "imagen"]

class AmericanasAleUpdate(UpdateView):
    model= AmericanasAle
    success_url= "/AppFinal/americanaAle/list"
    template_name = "americanasAle_form.html"
    fields = ["nombre", "maltas", "lupulo", "levadura", "adicionales", "procesoDeCoccion", "emailDeContacto", "fechaDePublicacion", "imagen"]

class AmericanasAleDelete(DeleteView):
    model= AmericanasAle
    template_name= "americanasAle_confirm_delete.html"
    success_url = "/AppFinal/americanasAle/list"


class AmericanasLagerList(ListView):
    model = AmericanasLager
    template_name= "americanasLager_list.html"

class AmericanasLagerDetalle(DetailView):
    model = AmericanasLager
    template_name= "americanasLager_detalle.html"
    context_object_name="americanasLager"

class AmericanasLagerCreacion(CreateView):
    model =AmericanasLager
    template_name= "americanasLager_form.html"
    succes_url= reverse_lazy ("AppFinal:list")
    fields = ["subCategoria","nombre", "maltas", "lupulo", "levadura", "adicionales", "procesoDeCoccion"]

class AmericanasLagerUpdate(UpdateView):
    model= AmericanasLager
    success_url= "/AppFinal/americanaLager/list"
    template_name = "americanasLager_form.html"
    fields = ["subCategoria","nombre", "maltas", "lupulo", "levadura", "adicionales", "procesoDeCoccion"]

class AmericanasLagerDelete(DeleteView):
    model= AmericanasLager
    template_name= "americanasLager_confirm_delete.html"
    success_url = "/AppFinal/americanasLager/list"