from django.db import models
# Create your models here.


class Ataque(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    tipo = models.ForeignKey('pokemon.TipoPokemon', on_delete=models.CASCADE)
    potencia = models.IntegerField(default=1)
    precision = models.IntegerField(default=10)

    def __str__(self):
        return self.nombre

