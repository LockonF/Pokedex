from rest_framework import serializers

from pokemon.models import Pokemon, TipoPokemon


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
