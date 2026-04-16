from django.shortcuts import render, redirect
from .forms import SolicitudForm


def registro_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save()
            return redirect('solicitudes:confirmacion', pk=solicitud.pk)
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/registro.html', {'form': form})


def confirmacion_solicitud(request, pk):
    from .models import Solicitud
    solicitud = Solicitud.objects.get(pk=pk)
    return render(request, 'solicitudes/confirmacion.html', {'solicitud': solicitud})
