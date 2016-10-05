from rest_framework import serializers

from entrenador.models import EntrenadorHasPokemon, Entrenador
from pokedex.models import Pokedex
from pokemon.serializers import CustomPokemonSerializer, PokemonSerializer


class EntrenadorHasPokemonSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Guardamos o modificamos (en caso de que exista) un objeto en el pokedex al capturar el pokemon
        Guardamos el pokemon capturado

        :param validated_data:
        :return:
        """

        try:
           obtenido = Pokedex.objects.get(entrenador=validated_data['entrenador'], pokemon=validated_data['pokemon'])
           obtenido.tiporegistro = 'Capturado'
           obtenido.save()
        except Pokedex.DoesNotExist:
            Pokedex(entrenador=validated_data['entrenador'],pokemon=validated_data['pokemon'],tiporegistro='Capturado').save()
        entrenador_pokemon = EntrenadorHasPokemon(**validated_data)
        entrenador_pokemon.save()
        return entrenador_pokemon

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
