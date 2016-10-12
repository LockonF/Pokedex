from rest_framework import serializers

from pokemon.models import Pokemon, TipoPokemon, Ataque


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class TipoPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPokemon
        fields = "__all__"

class AtaqueSerializer(serializers.ModelSerializer):
    poder = serializers.IntegerField(min_value=0)
    punteria = serializers.IntegerField(min_value=0,max_value=100)

    class Meta:
        model = Ataque
        fields = "__all__"

class CustomPokemonSerializer(serializers.ModelSerializer):
    tipo = TipoPokemonSerializer(read_only=True)

    class Meta:
        model = Pokemon
        fields = '__all__'
