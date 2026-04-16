from django.shortcuts import render
from .forms import AsistenciaForm
from .models import Asistencia


def asistencia_create(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save()  # ← guarda y captura el objeto
            return render(request, 'asistencia_success.html', {'asistencia': asistencia})
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia_form.html', {'form': form})


def asistencia_success(request):
    return render(request, 'asistencia_success.html')