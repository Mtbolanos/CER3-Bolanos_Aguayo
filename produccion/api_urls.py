from django.urls import path
from .api_views import ProduccionList

urlpatterns = [
    path('produccion/', ProduccionList.as_view(), name='produccion_list'),
]
