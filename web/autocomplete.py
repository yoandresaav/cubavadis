
from dal import autocomplete

from flights.models import SkyMarkets, Places


class SkyMarketsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated:
        #    return SkyMarkets.objects.none()

        qs = SkyMarkets.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs[:5]


class PlacesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Places.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs[:5]


class PlacesSpainAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Places.objects.filter(country_id="ES-sky")  # España
        if self.q:
            qs = qs.filter(place_name__istartswith=self.q)
        return qs[:5]

class PlacesCubaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Places.objects.filter(country_id="CU-sky")  # Cuba
        if self.q:
            qs = qs.filter(place_name__istartswith=self.q)
        return qs[:5]