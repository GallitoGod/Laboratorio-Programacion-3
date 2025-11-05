from django.urls import path
from . import views

app_name = 'informes'
urlpatterns = [
    path('inf_rec_activos/', views.informe_recorridos_activos, name='inf_rec_act')
]