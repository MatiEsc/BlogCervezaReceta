
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AmericanasAle(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion} "


class AlemanasChecasAustriacasAle(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion} "


class BelgasFrancesasAle(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion} "

class BritanicasAle(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion} "    


class InternacionalesAle(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion}"

class AmericanasLager(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion} "        


class AlemanasChecasAustriacasLager(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion}"

class InternacionalesLager(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion}"

class Otras(models.Model):
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)
    emailDeContacto=models.EmailField(null=True)
    fechaDePublicacion=models.DateTimeField(auto_now_add=True, null=True)
    imagen=models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return f" nombre: {self.nombre}- maltas: {self.maltas} - lupulo: {self.lupulo} - levadura: {self.levadura} - adicionales: {self.adicionales} - procesoDeCoccion: {self.procesoDeCoccion} - emailDeContacto:{self.emailDeContacto} - fechaDePublicacion:{self.fechaDePublicacion} "

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

