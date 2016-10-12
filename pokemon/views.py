from rest_framework import viewsets, generics

from pokemon.models import Pokemon, TipoPokemon, Ataque
from pokemon.serializers import PokemonSerializer, TipoPokemonSerializer, AtaqueSerializer


class PokemonViewset(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class TipoPokemonViewset(viewsets.ModelViewSet):
    serializer_class = TipoPokemonSerializer
    queryset = TipoPokemon.objects.all()

class AtaqueViewset(viewsets.ModelViewSet):
    serializer_class = AtaqueSerializer
    queryset = Ataque.objects.all()

class AtaqueMayorView(generics.ListAPIView):
    serializer_class = AtaqueSerializer
    queryset = Ataque.objects.filter(poder__gte=50)

class AtaqueMenorView(generics.ListAPIView):
    """
    muestra los ataques con poder menor o igual a 50
    """
    serializer_class = AtaqueSerializer
    queryset = Ataque.objects.filter(poder__lte=50)