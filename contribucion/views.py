from django.shortcuts import render, get_object_or_404
from contribucion.models import Autor, Trabajo



# Create your views here.
def mandadatos(request):
    trabajos = Trabajo.objects.all()
    autores = Autor.objects.order_by("orden")
    return render(request, 'carga_contribucion.html', {'trabajos':trabajos, 'autores': autores})

# def trabajo_detalle(request):
#     contribucion = Contribucion.objects.all()
#     #contribucion = Contribucion.objects.all()
#     return render(request, 'carga_contribucion.html',{'trabajo_detalle':trabajo_detalle})
#
#
# def detalle(request):
#     contribucion = Contribucion.objects.all()
#     participantes = contribucion.autores.all()
#
#     return render(request, 'carga_contribucion.html',{'contribucion': contribucion, 'participantes':participantes})