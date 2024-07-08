from rest_framework import generics
from .models import Produccion
from .serializers import ProduccionSerializer

class ProduccionList(generics.ListAPIView):
    serializer_class = ProduccionSerializer

    def get_queryset(self):
        planta = self.request.query_params.get('planta')
        producto = self.request.query_params.get('producto')
        fecha = self.request.query_params.get('fecha')
        queryset = Produccion.objects.all()
        if planta:
            queryset = queryset.filter(planta__nombre=planta)
        if producto:
            queryset = queryset.filter(producto__nombre=producto)
        if fecha:
            queryset = queryset.filter(fecha__year=fecha)
        return queryset