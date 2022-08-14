from rest_framework import serializers
from .models import materia


class materiaSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = materia
        fields = (
            'codigo', 'nombre',
            'creditos',  'horas_au', 'horas_cl'
        )



