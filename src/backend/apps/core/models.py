from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    f_nacimiento = models.DateField(blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.FileField(upload_to='avatars/', max_length=100, blank=True, default='avatars/default.jpg')