from rest_framework import serializers
from .models import postulantes

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = postulantes
        fields = ('id','nombre', 'dni', 'perfil', 'nivel', 'fecha_nacimiento')