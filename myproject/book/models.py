from django.db import models

# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
