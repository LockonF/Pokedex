from django.conf.urls import url
from rest_framework import routers

from ataque.views import AtaqueViewset, PokemonHasAtaqueViewset

router = routers.DefaultRouter(trailing_slash=False)


router.register(r'ataque', AtaqueViewset, 'ataque')
router.register(r'pokemon_has_ataque', PokemonHasAtaqueViewset, 'pokemon_has_ataque')


urlpatterns = [
]


urlpatterns += router.urls