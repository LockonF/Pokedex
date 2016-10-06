from rest_framework import serializers

from pokemon.models import Pokemon, TipoPokemon,PokemonHasAtaque
from rest_framework.exceptions import ValidationError


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class TipoPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPokemon
        fields = "__all__"


class CustomPokemonSerializer(serializers.ModelSerializer):
    tipo = TipoPokemonSerializer(read_only=True)

    class Meta:
        model = Pokemon
        fields = '__all__'


class PokemonHasAtaqueSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        tipopoke = attrs['pokemon']
        tipoataque = attrs['ataque']
        if tipopoke.tipo != tipoataque.tipo:
            raise ValidationError('No puedes asignar un ataque de tipo distinto al pokemon')
        else:
            return attrs

    class Meta:
        model = PokemonHasAtaque
        fields = '__all__'