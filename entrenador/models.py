from django.db import models
# Una app es un modulo
# Create your models here.
from pokemon.models import Pokemon


class Entrenador(models.Model):
    CHOICES = (('Mystic', 'Mystic'), ('Valor', 'Valor'), ('instinct', 'instinct'))
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)
    equipo = models.CharField(max_length=10, choices=CHOICES)
    pokemones = models.ManyToManyField(Pokemon,
                                       through='EntrenadorHasPokemon',
                                       through_fields=('entrenador','pokemon'))
    def __str__(self):
        return self.nombre


class EntrenadorHasPokemon(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField(default=1)
    hp = models.IntegerField(default=1)

    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

