from rest_framework import routers

from pokemon.views import PokemonViewset, TipoPokemonViewset

router = routers.DefaultRouter(trailing_slash=False)


router.register(r'pokemon', PokemonViewset, 'pokemon')
router.register(r'tipo_pokemon', TipoPokemonViewset, 'tipo_pokemon')


urlpatterns = [
]


urlpatterns += router.urls