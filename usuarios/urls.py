from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('mis_reservas/', views.mis_reservas, name='mis_reservas')
]