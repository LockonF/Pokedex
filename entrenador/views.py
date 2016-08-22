from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from entrenador.models import Entrenador, EntrenadorHasPokemon
from entrenador.serializers import EntrenadorHasPokemonSerializer, EntrenadorSerializer, EntrenadorPokemonSerializer


class EntrenadorViewset(viewsets.ModelViewSet):
    serializer_class = EntrenadorSerializer
    queryset = Entrenador.objects.all()


class EntrenadorHasPokemonViewset(viewsets.ModelViewSet):
    serializer_class = EntrenadorHasPokemonSerializer
    queryset = EntrenadorHasPokemon.objects.all()




class EntrenadorPokemonView(generics.ListAPIView):

    serializer_class = EntrenadorPokemonSerializer

    # Este método nos da el universo de objetos con el que trabaja el view
    def get_queryset(self):
        #Obtenemos el id del entrenador de la URL
        id_entrenador = self.kwargs['pk']

        # Get queryset debe de regresar un conjunto de objetos
        return EntrenadorHasPokemon.objects.filter(entrenador=id_entrenador)