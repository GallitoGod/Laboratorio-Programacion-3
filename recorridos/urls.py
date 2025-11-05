from django.urls import path
from . import views

app_name= 'recorridos'
urlpatterns = [
    path('formulario_recorrido/', views.recorrido_formulario, name='circuito_formulario'),
    path('lista_recorrido/', views.lista_circuito, name= 'circuito_listar'),
    path('editar_recorrido/<int:pk>/', views.editar_circuito, name= 'circuito_editar'),
    path('eliminar_recorrido/<int:pk>/', views.eliminar_circuito, name='circuito_eliminar'),
]