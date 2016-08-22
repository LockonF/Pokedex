from rest_framework import serializers

from entrenador.models import EntrenadorHasPokemon, Entrenador
from pokemon.serializers import CustomPokemonSerializer, PokemonSerializer


class EntrenadorHasPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrenadorHasPokemon
        fields = '__all__'


class EntrenadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrenador
        fields = ('id', 'nombre', 'nivel', 'equipo')


class EntrenadorPokemonSerializer(serializers.ModelSerializer):
    pokemon = CustomPokemonSerializer(read_only=True)

    class Meta:
        model = EntrenadorHasPokemon
        fields = ('id', 'cp', 'hp', 'nombre', 'pokemon')
