from django.urls import path
from . import views

app_name = 'reservas'
urlpatterns = [
    path('reserva_formulario/', views.reserva_formulario, name='reserva_formulario')
]