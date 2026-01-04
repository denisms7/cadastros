from django.contrib import admin
from django.urls import path, include
from .views import UsuarioDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UsuarioDetailView.as_view(template_name="base.html"), name="home"),  # MENU
    path('', include('register.urls')),
]
