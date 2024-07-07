from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produccion/', include('produccion.urls')),
    
    #path('api/', include('produccion.api_urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
]