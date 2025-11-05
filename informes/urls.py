from django.urls import path
from . import views

app_name = 'informes'
urlpatterns = [
    path('inf_rec_activos/', views.informe_recorridos_activos, name='inf_rec_act'),
    path('inf_rec_res/', views.informe_reservas_por_recorrido, name='inf_rec_res'),
    path('inf_par_conc/', views.informe_paradas_mas_concurridas, name='inf_par_conc'),
    path('inf_cant_pas_v/', views.cantidad_pasajeros_por_viaje, name='inf_cant_pas_v'),
    path('informe/', views.informes, name='informe'),
]