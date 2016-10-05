from django.db import models
from entrenador.models import Entrenador
from pokemon.models import Pokemon
# Create your models here.

class Pokedex(models.Model):
    CHOICES = (('Visto', 'Visto'), ('Capturado', 'Capturado'))
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokedex_pokemon')
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='pokedex_entrenador')
    tiporegistro = models.CharField(max_length=9, choices=CHOICES)

    class Meta:
        unique_together = ('entrenador','pokemon')

    def __str__(self): #representación en caracteres de un objeto en el modelo
        return self.nombre

