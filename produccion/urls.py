from django.urls import path
from .views import registrar_produccion, modificar_produccion, lista_produccion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrar/', registrar_produccion, name='registrar_produccion'),
    path('modificar/<int:pk>/', modificar_produccion, name='modificar_produccion'),
    path('', lista_produccion, name='lista_produccion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)