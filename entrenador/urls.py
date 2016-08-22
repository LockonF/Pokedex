from django.conf.urls import url
from rest_framework import routers

from entrenador.views import EntrenadorViewset, EntrenadorHasPokemonViewset, EntrenadorPokemonView

router = routers.DefaultRouter(trailing_slash=False)


router.register(r'entrenador', EntrenadorViewset, 'entrenador')
router.register(r'entrenador_has_pokemon', EntrenadorHasPokemonViewset, 'entrenador_has_pokemon')


urlpatterns = [

    ## Las vistas se registran en urlpatterns

    url(r'entrenador/pokemones/(?P<pk>[0-9+]$)',EntrenadorPokemonView.as_view())
]


urlpatterns += router.urls