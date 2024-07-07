from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produccion import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('produccion/', include('produccion.urls')),
    path('api/', include('produccion.api_urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.login_view, name = "login_view"),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)