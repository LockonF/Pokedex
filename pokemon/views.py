from rest_framework import viewsets

from pokemon.models import Pokemon, TipoPokemon
from pokemon.serializers import PokemonSerializer, TipoPokemonSerializer


class PokemonViewset(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class TipoPokemonViewset(viewsets.ModelViewSet):
    serializer_class = TipoPokemonSerializer
    queryset = TipoPokemon.objects.all()
