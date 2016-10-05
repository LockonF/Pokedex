from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics

from pokedex.models import Pokedex
from pokedex.serializers import PokedexSerializer


class PokedexViewset(viewsets.ModelViewSet):
    serializer_class = PokedexSerializer
    queryset = Pokedex.objects.all()

