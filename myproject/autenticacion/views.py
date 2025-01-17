from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .models import Usuario

from .forms import RegisterForm, LoginForm


def registroView(request: HttpRequest):
    """Vista para registrar un nuevo usuario."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('login') 
        else:
            if 'email' in form.errors:
                messages.error(request, "Este correo ya está en uso.")
            else:
                messages.error(request, "Hubo un error en el registro. Por favor, corrige los errores.")
    else:
        form = RegisterForm()
    return render(request, 'autenticacion/registro.html', {'form': form})

def loginView(request: HttpRequest):
    """Vista para iniciar sesión."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #hay un problema aquí
            user = Usuario.objects.get(username=username, password=password)
            print(authenticate(request, username=username))
            if user is not None:
                login(request, user)
                messages.success(request, '¡Bienvenido de nuevo!')
        elif 'user' in form.cleaned_data:
            messages.error(request, 'Error de credenciales.')
    else:
        form = LoginForm()

    return render(request, 'autenticacion/login.html', {'form': form})


def logoutView(request: HttpRequest):
    """Vista para cerrar sesión."""
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return render(request, 'autenticacion/logout.html')