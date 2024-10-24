from django.contrib import admin
from robot.adapters.persistence.models import SecuenciaMovimiento

@admin.register(SecuenciaMovimiento)
class SecuenciaMovimientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'movimientos', 'fechacreado')  # Campos que se mostrarán en la lista
    search_fields = ('titulo',)  # Permite buscar por título


# Register your models here.
