from django.shortcuts import render
from .forms import AsistenciaForm
from .models import Asistencia


def asistencia_create(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'asistencia_success.html')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia_form.html', {'form': form})


def asistencia_success(request):
    return render(request, 'asistencia_success.html')