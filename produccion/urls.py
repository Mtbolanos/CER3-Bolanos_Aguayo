from django.urls import path
from .views import registrar_produccion, modificar_produccion, lista_produccion, registro

urlpatterns = [
    path('registrar/', registrar_produccion, name='registrar_produccion'),
    path('modificar/<int:pk>/', modificar_produccion, name='modificar_produccion'),
    path('', lista_produccion, name='lista_produccion'),
    path('registro/', registro, name='registro'),
]
