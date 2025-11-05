from django.urls import path
from . import views

app_name = 'colectivos'
urlpatterns = [
    path('formulario_colectivo/', views.formulario_colectivo, name= 'colectivo_formulario'),
    path('lista_colectivo/', views.lista_colectivo, name= 'colectivo_listar'),
    path('editar_colectivo/<int:pk>/editar/', views.editar_colectivo, name= 'colectiva_editar'),
    path('itinerarios/<int:pk>/eliminar/', views.eliminar_colectivo, name='itinerario_eliminar'),
]