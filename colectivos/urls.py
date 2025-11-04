from django.urls import path
from . import views

app_name = 'colectivos'
urlpatterns = [
    path('formulario_colectivo/', views.formulario_colectivo, name='colectivo_formulario')
]