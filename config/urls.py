from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mascotas/', views.listaMascota, name="listaMascota"),
    path('mascotas/detalle/<int:id>/', views.detalleMascota, name="detalleMascota"),
]
