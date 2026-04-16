from . import views
from django.urls import path

urlpatterns = [
    path('newAsistencia/', views.asistencia_create, name='asistencia_new'),
    path('successAsistencia/', views.asistencia_success, name='asistencia_success'),
]