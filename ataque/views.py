from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics

from ataque.models import Ataque
from ataque.serializers import AtaqueSerializer
from pokemon.serializers import PokemonHasAtaqueSerializer
from pokemon.models import PokemonHasAtaque

class AtaqueViewset(viewsets.ModelViewSet):
    serializer_class = AtaqueSerializer
    queryset = Ataque.objects.all()


class PokemonHasAtaqueViewset(viewsets.ModelViewSet):
    serializer_class = PokemonHasAtaqueSerializer
    queryset = PokemonHasAtaque.objects.all()