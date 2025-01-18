from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el libro en la base de datos
            return render(request, 'book/success.html', {'form': form})
    else:
        form = BookForm()
    return render(request, 'book/inputbook.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'autenticacion/login.html'
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = 'autenticacion/logout.html'


@permission_required('book.development', raise_exception=True)
def developer_view(request):
    return HttpResponse("Tienes acceso como Desarrollador.")