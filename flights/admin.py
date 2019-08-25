# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Continent, Country, Municipality, TipoAirport, Airport


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_country', 'continent', 'name')
    list_filter = ('continent',)
    search_fields = ('name',)


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_region', 'municipality', 'country')
    list_filter = ('country',)


@admin.register(TipoAirport)
class TipoAirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'air_id',
        'ident',
        'name',
        'latitude_deg',
        'longitude_deg',
        'elevation_ft',
        'scheduled_service',
        'gps_code',
        'iata_code',
        'local_code',
        'wikipedia_link',
        'keywords',
        'slug',
    )
    list_filter = ('tipo', 'scheduled_service')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}