from django.db import models


# Create your models here.
class TipoPokemon(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ataque(models.Model):
    nombre = models.CharField(max_length=50)
    poder = models.IntegerField()
    punteria = models.IntegerField()
    tipo_pokemon = models.ForeignKey(TipoPokemon, on_delete=models.CASCADE, related_name='ataque_tipo')

    def __str__(self):
        return self.nombre

class Pokemon(models.Model):
    CHOICES = (('normal', 'normal'), ('legenario', 'legendario'))
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoPokemon, on_delete=models.CASCADE)
    is_legendario = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.nombre
