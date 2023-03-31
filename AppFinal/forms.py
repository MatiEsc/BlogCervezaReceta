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


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField (label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField (label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", 'password1' , 'password2']
        #help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model= User
        fields= ["imagen"]
        help_texts= {k:"" for k in fields}


