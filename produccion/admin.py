from django.contrib import admin
from .models import Planta, Producto, Produccion

def anular_produccion(modeladmin, request, queryset):
    queryset.update(anulado=True, anulado_por=request.user, anulado_el=timezone.now())

anular_produccion.short_description = "Anular producción seleccionada"

class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'litros', 'fecha', 'turno', 'hora_registro', 'operador')
    list_filter = ('producto', 'fecha', 'turno')
    search_fields = ('producto__nombre', 'fecha', 'turno')

admin.site.register(Produccion, ProduccionAdmin)
admin.site.register(Planta)
admin.site.register(Producto)
