
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UsuarioviewSet, Tipo_UsuarioViewSet, Estado_TareaViewSet, TareaViewSet, reporte1ViewSet

router = DefaultRouter()
router.register(r'usuario', UsuarioviewSet)
router.register(r'tipo_usuario', Tipo_UsuarioViewSet)
router.register(r'estado_tarea', Estado_TareaViewSet)
router.register(r'tarea', TareaViewSet)
router.register(r'reportes', reporte1ViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]


