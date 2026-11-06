from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mascotas/', views.listaMascota, name="listaMascota"),
    path('mascotas/detalle/<int:id>/', views.detalleMascota, name="detalleMascota"),
    path('gestion-mascotas/', views.gestionListarMascotas, name="gestionListarMascotas"),
    path('gestion-mascotas/agregar/', views.gestionAgregarMascota, name="gestionAgregarMascota"),
    path('gestion-mascotas/modificar/<int:id>/', views.gestionModificarMascota, name="gestionModificarMascota"),
    path('gestion-mascotas/eliminar/<int:id>/', views.gestionEliminarMascota, name='gestionEliminarMascota'),
]
