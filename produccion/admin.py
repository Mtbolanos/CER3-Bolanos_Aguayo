from django.contrib import admin
from .models import Planta, Producto, Produccion
from django.utils import timezone

def anular_produccion(modeladmin, request, queryset):
    queryset.update(anulado=True, anulado_por=request.user, anulado_el=timezone.now())

anular_produccion.short_description = "Anular producción seleccionada"

class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('planta', 'producto', 'cantidad', 'fechahora', 'operador' , 'modificado_por', 'modificado_el', 'anulado', 'anulado_por', 'anulado_el')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='operador').exists():
            return qs.filter(operador=request.user)
        return qs
    
    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user.groups.filter(name='operador').exists():
            return obj.operador == request.user
        return super().has_change_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user.groups.filter(name='operador').exists():
            return obj.operador == request.user
        return super().has_delete_permission(request, obj)
    
admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(Produccion, ProduccionAdmin)

