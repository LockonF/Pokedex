from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pokedex.models import Pokedex


class PokedexSerializer(serializers.ModelSerializer):


    class Meta:
        model = Pokedex
        fields = ('id','pokemon', 'entrenador', 'tiporegistro')

    def validate(self, attrs):
        if attrs['tiporegistro'].lower() == 'visto':
            raise ValidationError('No podemos guardar pokemones en visto, que groseros')
