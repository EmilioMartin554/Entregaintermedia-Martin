from django.db import models
class libro(models.Model):
    fecha_de_publicacion=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
class revista(models.Model):
    fecha_de_publicacion=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
class texto(models.Model):
    fecha_de_publicacion=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    link=models.CharField(max_length=2000)
# Create your models here.
