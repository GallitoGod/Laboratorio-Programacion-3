from django.urls import path
from . import views

app_name = 'itinerarios'
urlpatterns = [
    path('formulario_itinerario/', views.formulario_itinerario, name='itinerario_formulario'),
    path('formulario_pd/', views.formulario_punto_destacado, name='pd_formulario'),
    path('formulario_parada/', views.formulario_parada, name='parada_formulario'),
    path('formulario_it_detalle/<int:pk>/', views.detalles_itinerario, name='itinerario_detalle'),
    path('lista_itinerario/', views.lista_itinerario, name= 'itinerario_listar'),
    path('editar_itinerario/<int:pk>/', views.editar_itinerario, name= 'itinerario_editar'),
    path('eliminar_itinerario/<int:pk>/', views.eliminar_itinerario, name='itinerario_eliminar'),
    path('lista_parada/', views.lista_parada, name= 'parada_listar'),
    path('editar_parada/<int:pk>/', views.editar_parada, name= 'parada_editar'),
    path('eliminar_parada/<int:pk>/', views.eliminar_parada, name='parada_eliminar'),
    path('lista_pd/', views.lista_punto_destacado, name= 'pd_listar'),
    path('editar_pd/<int:pk>/', views.editar_punto_destacado, name= 'pd_editar'),
    path('eliminar_pd/<int:pk>/', views.eliminar_punto_destacado, name='pd_eliminar'),
]