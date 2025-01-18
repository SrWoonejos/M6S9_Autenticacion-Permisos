from django.db.models.signals import post_save
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_development_permission(sender, instance, created, **kwargs):
    """
    Asigna automáticamente el permiso 'book.development' al usuario
    cuando se crea un nuevo usuario.
    """
    if created:  # Solo se ejecuta cuando el usuario es recién creado
        # Obtén el permiso 'book.development'
        try:
            permiso_developer = Permission.objects.get(codename='development')
            # Asigna el permiso al usuario
            instance.user_permissions.add(permiso_developer)
        except Permission.DoesNotExist:
            print("El permiso 'book.development' no existe. Asegúrate de haberlo definido correctamente en el modelo.")