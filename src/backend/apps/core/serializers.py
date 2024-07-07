from rest_framework import serializers
from apps.core.models import Persona

class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField() 
    f_nacimiento=serializers.CharField()
    ciudad = serializers.CharField()
    avatar = serializers.FileField()
    class Meta:
        model = Persona 