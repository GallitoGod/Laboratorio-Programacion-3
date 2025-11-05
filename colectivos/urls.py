from django.urls import path
from . import views

app_name = 'colectivos'
urlpatterns = [
    path('formulario_colectivo/', views.formulario_colectivo, name= 'colectivo_formulario'),
    path('lista_colectivo/', views.lista_colectivo, name= 'colectivo_listar'),
    path('editar_colectivo/<int:pk>/', views.editar_colectivo, name= 'colectivo_editar'),
    path('eliminar_colectivo/<int:pk>/', views.eliminar_colectivo, name='colectivo_eliminar'),
]