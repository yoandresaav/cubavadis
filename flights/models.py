from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Continent(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    iso_country = models.CharField(max_length=2)
    continent = models.ForeignKey(
        Continent, on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=340)

    def __str__(self):
        return self.iso_country


class Municipality(models.Model):
    iso_region = models.CharField(max_length=10)
    municipality = models.CharField(max_length=60)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.municipality


class TipoAirport(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo


class Airport(models.Model):
    air_id = models.CharField(max_length=6)
    ident = models.CharField(max_length=8)
    tipo = models.ForeignKey(TipoAirport, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=260)
    latitude_deg = models.DecimalField(
        max_digits=22, decimal_places=16, default=0
    )
    longitude_deg = models.DecimalField(
        max_digits=22, decimal_places=16, default=0
    )
    elevation_ft = models.SmallIntegerField(default=0)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.SET_NULL, null=True
    )
    scheduled_service = models.BooleanField(default=False)
    gps_code = models.CharField(max_length=8, blank=True, null=True)
    iata_code = models.CharField(max_length=14, blank=True, null=True)
    local_code = models.CharField(max_length=14, blank=True, null=True)
    wikipedia_link = models.URLField(blank=True, null=True)
    keywords = models.CharField(max_length=320, blank=True, null=True)
    slug = models.SlugField(max_length=140, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # If no exist data genero random slug
        check_if_slug_exist(self)
        super().save(*args, **kwargs)


def check_if_slug_exist(obj):
    name = obj.name or get_random_string(8)
    local_code = obj.local_code or get_random_string(8)
    while True:
        slug = '%s-%s' % (slugify(name), slugify(local_code))
        air_query = Airport.objects.filter(slug=slug)
        if not air_query.exists():
            obj.slug = slug
            break
        name = get_random_string(8)
        local_code = get_random_string(8)
