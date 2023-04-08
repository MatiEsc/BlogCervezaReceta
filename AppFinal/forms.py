from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone 


class AmericanasAleFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class AlemanasChecasAustriacasAleFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class BelgasFrancesasAleFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class BritanicasAleFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class InternacionalesAleFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class AmericanasLagerFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class AlemanasChecasAustriacasLagerFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class InternacionalesLagerFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

class OtrasFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    maltas=forms.CharField(max_length=40)
    lupulo=forms.CharField(max_length=40)
    levadura=forms.CharField(max_length=40)
    adicionales=forms.CharField(max_length=40)
    proceso_De_Coccion=forms.CharField(max_length=200)
    email_De_Contacto=forms.EmailField()
    fecha_De_Publicacion=forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput())
    imagen = forms.ImageField(required=False)

