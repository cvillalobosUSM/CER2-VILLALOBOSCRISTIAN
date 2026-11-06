from django.shortcuts import redirect, render, get_object_or_404
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

#################################

@login_required
@permission_required('core.view_mascota', raise_exception=True)
def gestionListarMascotas(request):
    mascotas = Mascota.objects.all()
    context = {
        "mascotas": mascotas,
    }
    return render(request, 'core/gestionMascotas.html', context)

@login_required
@permission_required('core.add_mascota', raise_exception=True)
def gestionAgregarMascota(request):
    especies = Especie.objects.all()

    if request.method=="POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        sexo = request.POST.get("sexo")
        edadAproximada = request.POST.get("edadAproximada")
        imagen = request.POST.get("imagen")
        especieID = request.POST.get("especie")

        especie = get_object_or_404(Especie, id=especieID)

        Mascota.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            sexo=sexo,
            edadAproximada=edadAproximada,
            imagen=imagen,
            especie=especie
        )

        return redirect('gestionListarMascotas')

    context = {
        "especies": especies,
    }
    return render(request, 'core/agregarMascota.html', context)

@login_required
@permission_required('core.change_mascota', raise_exception=True)
def gestionModificarMascota(request,id):
    mascota = get_object_or_404(Mascota, id=id)
    especies = Especie.objects.all()

    if request.method == 'POST':

            mascota.nombre = request.POST.get('nombre')
            mascota.descripcion = request.POST.get('descripcion')
            mascota.sexo = request.POST.get('sexo')
            mascota.edadAproximada = request.POST.get('edadAproximada')
            mascota.imagen = request.POST.get('imagen')
            especieID = request.POST.get('especie')
            mascota.especie = get_object_or_404(Especie, id=especieID)
            mascota.save()

            return redirect('gestionListarMascotas')

    context = {
        'mascota': mascota,
        'especies': especies,
    }
    return render(request, 'core/modificarMascota.html', context)

@login_required
@permission_required('core.delete_mascota', raise_exception=True)
def gestionEliminarMascota(request, id):
    if request.method == 'POST':
        mascota = get_object_or_404(Mascota, id=id)
        mascota.delete()

    return redirect('gestionListarMascotas')
