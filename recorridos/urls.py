from django.urls import path
from . import views

app_name= 'recorridos'
urlpatterns = [
    path('recorrido_formulario/', views.recorrido_formulario, name='recorrido_formulario')
]