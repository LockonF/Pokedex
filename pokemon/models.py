from django.db import models
from ataque.models import Ataque

# Create your models here.
class TipoPokemon(models.Model):
    CHOICES = (('Agua', 'Agua'), ('Fuego', 'Fuego'), ('Planta', 'Planta'))
    nombre = models.CharField(max_length=50,choices=CHOICES,unique=True)

    def __str__(self):
        return self.nombre


class Pokemon(models.Model):
    CHOICES = (('normal', 'normal'), ('legenario', 'legendario'))
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoPokemon, on_delete=models.CASCADE, related_name='pokemon_has_tipo')
    is_legendario = models.CharField(max_length=20, choices=CHOICES)
    ataques = models.ManyToManyField(Ataque,
                                       through='PokemonHasAtaque',
                                       through_fields=('pokemon', 'ataque'),related_name='pokemon_has_ataque')
    def __str__(self):
        return self.nombre


class PokemonHasAtaque(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                   related_name='pokemon_has_ataque_pokemon')
    ataque = models.ForeignKey(Ataque, on_delete=models.CASCADE, related_name='ataque_has_pokemon_pokemon')

    def __str__(self):
        return self.nombre