from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('core:landing')
        else:
            return render(request, "usuarios/login.html", {"msj": "Credenciales incorrectas"})
    return redirect('core:landing') 

def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {"msj": "Deslogueado"})
