from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Publicaciones(models.Model):
    autor = models.CharField(max_length = 30)
    titulo = models.CharField(max_length = 100)
    contenido = models.TextField()
    
   
          
class About(models.Model):
          
          fechaDePublicacion = models.DateField()
          contenido = models.CharField(max_length=500)
          

class Avatar(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     imagen=models.ImageField(upload_to = 'avatares', null=True, blank=True)
     

     class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
        
        
class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    identificacion = models.IntegerField()
    area = models.CharField(max_length=100)


    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.identificacion,self.nombre)


class Colaborador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")

    def __str__(self):
        txt="{0} , {1}"
        return txt.format(self.apellido,self.nombre)

class Lider(models.Model):


    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Area: {self.area} - Email: {self.email} "


    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    area = models.CharField(max_length=100)
    email = models.EmailField()


    class Meta:
        verbose_name = "Lider"
        verbose_name_plural = "Lideres"


