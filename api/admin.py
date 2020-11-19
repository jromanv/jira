from django.contrib import admin
from .models import Usuario, Tipo_Usuario, Tarea, Estado_Tarea

admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Tarea)
admin.site.register(Estado_Tarea)

# Register your models here.
