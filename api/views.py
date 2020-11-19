from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Tipo_Usuario, Tarea, Estado_Tarea
from .serializers import UsuarioSerializer, Tipo_UsuarioSerializer, TareaSerializer, Estado_TareaSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, filters
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count, Case, When, Sum, Q

class Tipo_UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = Tipo_UsuarioSerializer
    queryset = Tipo_Usuario.objects.all()

class UsuarioviewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class Estado_TareaViewSet(viewsets.ModelViewSet):
    serializer_class = Estado_TareaSerializer
    queryset = Estado_Tarea.objects.all()

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()


class reporte1ViewSet(GenericViewSet):
    queryset = Usuario.objects.all()

    @action(methods=['get'],detail=False)

    def reporte1(self,request):
        try:
            '''Usuario_responsable = Usuario.objects.filter(id_tipo_usuario__nombre='Responsable').count()'''
            tareas_usuario_responsable = (Tarea.objects
                                            .filter(id_usuario__id_tipo_usuario__nombre='Responsable')).count()
            tarea_estado1 = (Tarea.objects
                                            .filter(id_usuario__id_tipo_usuario__nombre='Responsable')
                                            .filter(id_estado_tarea__nombre='Por Hacer')).count()

            tarea_estado2 = (Tarea.objects
                                            .filter(id_usuario__id_tipo_usuario__nombre='Responsable')
                                            .filter(id_estado_tarea__nombre='Haciendo')).count()
            
            tarea_estado3 = (Tarea.objects
                                            .filter(id_usuario__id_tipo_usuario__nombre='Responsable')
                                            .filter(id_estado_tarea__nombre='Hecho')).count()                                            
                                            
            rep = {'Tareas_usuario_res':tareas_usuario_responsable,
                   'Total tareas por Hacer':tarea_estado1,
                   'Total tareas haciendo':tarea_estado2,
                   'Total tareas hechas':tarea_estado3}
            return Response({'Reporte 1':rep},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detalle':str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'],detail=False)
    def reporte2(self,request):
        try:            
            tarea_estado1 = (Tarea.objects                                            
                                            .filter(id_estado_tarea__nombre='Por Hacer')).count()

            tarea_estado2 = (Tarea.objects                                           
                                            .filter(id_estado_tarea__nombre='Haciendo')).count()
            
            tarea_estado3 = (Tarea.objects                                        
                                            .filter(id_estado_tarea__nombre='Hecho')).count()                                            
                                            
            rep = {'Total tareas por Hacer':tarea_estado1,
                   'Total tareas haciendo':tarea_estado2,
                   'Total tareas hechas':tarea_estado3}
            return Response({'Reporte 2':rep},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detalle':str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'],detail=False)
    def reporte3(self,request):
        try:         
            tarea_estado = Tarea.objects.all().count()

            tarea_estado1 = (Tarea.objects.filter(id_estado_tarea__nombre='Por Hacer')).count()

            tarea_estado2 = (Tarea.objects .filter(id_estado_tarea__nombre='Haciendo')).count()
            
            tarea_estado3 = (Tarea.objects.filter(id_estado_tarea__nombre='Hecho')).count()                                            

            porcentaje_hacer = (tarea_estado1/tarea_estado)*100
            porcentaje_haciendo = (tarea_estado2/tarea_estado)*100 
            porcentaje_hecho = (tarea_estado3/tarea_estado)*100  

            rep = {'Total Tareas':tarea_estado,
                   'Porcentaje tareas por Hacer':int(porcentaje_hacer),
                   'Porcentaje tareas haciendo':int(porcentaje_haciendo),
                   'Porcentaje tareas hechas':int(porcentaje_hecho)}
            return Response({'Reporte 3':rep},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detalle':str(e)}, status=status.HTTP_400_BAD_REQUEST)


