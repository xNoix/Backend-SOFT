from django.contrib import admin
from robot.adapters.persistence.models import RobotDatos, SecuenciaMovimiento

@admin.register(SecuenciaMovimiento)
class SecuenciaMovimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tipo', 'movimientos', 'fechacreado')  # Campos que se mostrarán en la lista
    search_fields = ('titulo',)  # Permite buscar por título

@admin.register(RobotDatos)
class RobotDatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ip', 'minH', 'minmaxJoints')
    search_fields = ('nombre',)  # Permite buscar por nombre

# Register your models here.
