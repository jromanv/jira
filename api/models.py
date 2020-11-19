from django.db import models
#Aqui se define la tabla de tipos de usuarios que puede ser administrador y responsable
class Tipo_Usuario(models.Model):
    nombre = models.CharField(max_length=20, blank=False)
    
    class Meta:
        verbose_name = 'Tipo de Usuario'
        verbose_name_plural = 'Tipos de Usuarios'

    def __str__(self):
        return self.nombre

#Clase de Estados de tareas que pueden ser por hacer, haciendo y hecho
class Estado_Tarea(models.Model):
    nombre = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Estado de Tarea'
        verbose_name_plural = 'Estado de Tareas'
     
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=40)
    #Relación entre tabla Usuario y Tipo Usuario
    id_tipo_usuario = models.ForeignKey(Tipo_Usuario, null=True, blank=True, on_delete=models.CASCADE)
  
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    descripcion = models.TextField()
    apertura = models.DateTimeField(auto_now_add=True)
    cierre = models.DateTimeField(auto_now=False)
    id_usuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete=models.CASCADE)
    id_estado_tarea = models.ForeignKey(Estado_Tarea, null = True, blank = True, on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = 'Tarea' 
        verbose_name_plural = 'Tareas'
           
    def __str__(self):
        return self.descripcion


 
  



