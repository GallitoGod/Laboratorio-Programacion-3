from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from reservas.models import Reserva
from django.utils import timezone
from django.urls import reverse

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:landing')

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next') or reverse('core:landing')
            return redirect(next_url)
        return render(request, "usuarios/login.html", {"msj": "Credenciales incorrectas"})

    return render(request, "usuarios/login.html") 

def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {"msj": "Deslogueado"})

def mis_reservas(request):
    if not request.user.is_authenticated:
        return render(request, 'reservas.html', {
            'reservas': [],
            'mensaje': 'Debes iniciar sesiÃ³n para ver tus reservas.'
        })

    if request.method == 'POST':
        reserva_id = request.POST.get('reserva_id')
        r = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
        if r.fecha >= timezone.now().date():
            if r.colectivo_id is not None:
                c = r.colectivo
                c.cant_ocupados = max(0, (c.cant_ocupados or 0) - (r.cantCupos or 0))
                c.save(update_fields=['cant_ocupados'])
            r.delete()
        return redirect('usuarios:mis_reservas')

    reservas = Reserva.objects.filter(usuario=request.user).order_by('-fecha')

    return render(request, 'reservas.html', {
        'reservas': reservas,
        'hoy': timezone.now().date(),
    })