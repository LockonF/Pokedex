from django.conf.urls import url
from rest_framework import routers

from pokedex.views import PokedexViewset

router = routers.DefaultRouter(trailing_slash=False)


router.register(r'pokedex', PokedexViewset, 'pokedex')


urlpatterns = [
]


urlpatterns += router.urls