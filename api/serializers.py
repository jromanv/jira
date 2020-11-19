from rest_framework import serializers
from .models import Usuario, Tipo_Usuario, Tarea, Estado_Tarea

#Converitr modelo Tipo_Usuario a Formato Json
class Tipo_UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Usuario
        fields = '__all__'

#Converitr modelo Usuario a Formato Json
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

#Converitr modelo Estado_Tarea a Formato Json
class Estado_TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Tarea
        fields = '__all__'

#Converitr modelo Tarea a Formato Json
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'



























