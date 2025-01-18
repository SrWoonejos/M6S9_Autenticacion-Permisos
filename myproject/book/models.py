from django.db import models

# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valor = models.IntegerField()
    published_date = models.DateField(default='2000-01-01')

    class Meta:
        # Definimos los permisos personalizados
        permissions = [
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como Scrum Master'),
            ('product_owner', 'Permiso como Product Owner'),
        ]

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
