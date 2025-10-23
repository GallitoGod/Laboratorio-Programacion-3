from django.urls import path
from . import views


app_name = 'avisos'
urlpatterns = [
    path('', views.home, name='landing')
]