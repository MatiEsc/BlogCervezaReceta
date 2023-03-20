from django.db import models

# Create your models here.
class AmericanasAle(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class AlemanasChecasAustriacasAle(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class BelgasFrancesasAle(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class BritanicasAle(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class InternacionalesAle(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class Americanaslager(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class AlemanasChecasAustriacasLager(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class InternacionalesLager(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)

class Otras(models.Model):
    subCategoria= models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    maltas=models.CharField(max_length=40)
    lupulo=models.CharField(max_length=40)
    levadura=models.CharField(max_length=40)
    adicionales=models.CharField(max_length=40)
    procesoDeCoccion=models.CharField(max_length=200)