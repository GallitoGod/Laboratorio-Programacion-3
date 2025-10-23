from django.urls import path
from . import views

app_name= 'recorridos'
urlpatterns = [
    path('formulario_recorrido/', views.formulario_recorrido, name='formulario_recorrido')
]