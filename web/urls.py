from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from .views import (
    HomeView, ToursView, AboutView, GalleryView,
    BlogView, ContactsView, SearchFlights,
    ResultadosVuelosView
)
from .api import send_form_vuelos, retornador_respuesta_vuelos

from .autocomplete import (
    PlacesAutocomplete,
    PlacesSpainAutocomplete,
    PlacesCubaAutocomplete,
    SkyMarketsAutocomplete,
)

app_name = 'web'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search-flights/', SearchFlights.as_view(), name='search-flights'),
    path(_('tours/'), ToursView.as_view(), name='tours'),
    path('about/', AboutView.as_view(), name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    

    path('vuelos/<str:perfil>/', ResultadosVuelosView.as_view(), name='resultados_vuelos'),

    # api
    path('send_form_vuelos/', send_form_vuelos, name='send_form_vuelos'),
    path('retornador_respuesta_vuelos/', retornador_respuesta_vuelos, name='retornador_respuesta_vuelos'),
    # autocompletes
    path('skymarkets-autocomplete/', SkyMarketsAutocomplete.as_view(), name='skymarkets-autocomplete'),
    path('places-autocomplete/', PlacesAutocomplete.as_view(), name='places-autocomplete'),
    path('places-spain-autocomplete/', PlacesSpainAutocomplete.as_view(), name='places-spain-autocomplete'),
    path('places-cuba-autocomplete/', PlacesCubaAutocomplete.as_view(), name='places-cuba-autocomplete'),
]
