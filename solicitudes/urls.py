from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('registro/', views.registro_solicitud, name='registro'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion'),
]
