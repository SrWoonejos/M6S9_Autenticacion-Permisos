from django.contrib import admin
from .models import Book

# Configuración del modelo en el admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista del admin
    list_display = ('titulo', 'autor', 'published_date')
    # Campos para filtrar en la barra lateral
    list_filter = ('autor', 'published_date')
    # Campos para buscar en la barra de búsqueda
    search_fields = ('titulo', 'autor')
