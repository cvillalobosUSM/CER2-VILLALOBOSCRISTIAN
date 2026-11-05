from django.shortcuts import render, get_object_or_404
from .models import Especie, Mascota
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    return render(request, 'core/home.html')

def listaMascota(request):
    mascotas = Mascota.objects.select_related('especie').all()
    especies = Especie.objects.all()

    especieSeleccionada = request.GET.get('especie')
    nombreEspecie = "Todas nuestras mascotas"
    if especieSeleccionada:
        mascotas = mascotas.filter(especie_id=especieSeleccionada)
        nombreEspecie = (get_object_or_404(Especie, id=especieSeleccionada)).nombre
        nombreEspecie = "Mostrando solo: " + nombreEspecie
    context = {
        'mascotas': mascotas,
        'especies': especies,
        'especieSeleccionada': especieSeleccionada,
        'nombreEspecieSeleccionada': nombreEspecie,
    }
    return render(request, 'core/listaMascota.html', context)

def detalleMascota(request,id):
    mascota = get_object_or_404(Mascota, id=id)
    context = {
        'mascota': mascota
    }
    return render(request, 'core/detalleMascota.html', context)

@login_required
@permission_required([
    'core.view_mascota',
    'core.add_mascota',
    'core.change_mascota',
    'core.delete_mascota'
], raise_exception=True)
def gestionMascotas(request):
    mascotas = Mascota.objects.all()
    context = {
        "mascotas": mascotas,
    }

    return render(request, 'core/gestionMascotas.html', context)
