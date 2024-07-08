from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    f_nacimiento = models.DateField(blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.FileField(upload_to='avatars/', max_length=100, blank=True, default='avatars/default.jpg')



class Pregunta(models.Model):
    texto = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.texto
    


class DatosEntrenamiento(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pregunta
    

class Conversacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    respuesta = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversación con {self.usuario.username} en {self.fecha_creacion}"


