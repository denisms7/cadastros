from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastros.urls')),
    path('', include('nav_bar.urls')),
]
