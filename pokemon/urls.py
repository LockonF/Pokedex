from rest_framework import routers
from django.conf.urls import url
from pokemon.views import PokemonViewset, TipoPokemonViewset, AtaqueViewset, AtaqueMayorView, AtaqueMenorView

router = routers.DefaultRouter(trailing_slash=False)


router.register(r'pokemon', PokemonViewset, 'pokemon')
router.register(r'tipo_pokemon', TipoPokemonViewset, 'tipo_pokemon')
router.register(r'ataque', AtaqueViewset, 'ataque')

urlpatterns = [
    url(r'ataque/mayor$',AtaqueMayorView.as_view()),
    url(r'ataque/menor$',AtaqueMenorView.as_view())
]


urlpatterns += router.urls