from rest_framework import serializers
from .models import Produccion

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'
