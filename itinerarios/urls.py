from django.urls import path
from . import views

app_name = 'itinerarios'
urlpatterns = [
    path('formulario_itinerario/', views.formulario_itinerario, name='itinerario_formulario'),
    path('formulario_pd/', views.formulario_punto_destacado, name='pd_formulario'),
    path('formulario_parada/', views.formulario_parada, name='parada_formulario'),
    path('formulario_it_detalle/<int:pk>/', views.detalles_itinerario, name='itinerario_detalle')
]