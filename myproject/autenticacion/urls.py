from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registroView, name='registro'),  # Ruta para el registro
    path('login/', views.loginView, name='login'),  # Ruta para iniciar sesión
    path('logout/', views.logoutView, name='logout'),  # Ruta para cerrar sesión
]