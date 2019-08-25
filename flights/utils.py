from .models import (
    Airport,
    Country,
    Continent,
    TipoAirport,
    Municipality,
)

ID = 0
IDENT = 1
TYPE = 2
NAME = 3
LATITUDE_DEG = 4
LONGITUDE_DEG = 5
ELEVATION_FT = 6
CONTINENT = 7
ISO_COUNTRY = 8
ISO_REGION = 9
MUNICIPALITY = 10
SCHEDULED_SERVICE = 11
GPS_CODE = 12
IATA_CODE = 13
LOCAL_CODE = 14
HOME_LINK = 15
WIKIPEDIA_LINK = 16
KEYWORDS = 17


def return_id_create_o_get_type(type_value):
    obj, _ = TipoAirport.objects.get_or_create(
        tipo=type_value
    )
    return obj


def create_continent(code, name=''):
    """
    code
    name
    """
    obj, _ = Continent.objects.get_or_create(
        code=code,
        name=name
    )
    return obj


def create_country(row):
    """
    iso_country
    continent
    name
    """
    continent_name = row[CONTINENT]
    continent = create_continent(code=continent_name)

    iso_country = row[ISO_COUNTRY]
    name = row[NAME]

    obj, _ = Country.objects.get_or_create(
        iso_country=iso_country,
        continent=continent,
        name=name
    )
    return obj


def create_municipality(row):
    """
    iso_region
    municipality
    country
    """
    municipality = row[MUNICIPALITY]
    iso_region = row[ISO_REGION]

    country = create_country(row)

    obj, _ = Municipality.objects.get_or_create(
        iso_region=iso_region,
        municipality=municipality,
        country=country
    )

    return obj


def create_airport(row):
    scheduled_service = True if row[SCHEDULED_SERVICE] == 'yes' else False
    airport_type = return_id_create_o_get_type(row[TYPE])
    municipality = create_municipality(row)
    Airport.objects.create(
        tipo=airport_type,
        municipality=municipality,
        # CHAR
        ident=row[ID],
        name=row[NAME],
        gps_code=row[GPS_CODE],
        iata_code=row[IATA_CODE],
        local_code=row[LOCAL_CODE],
        wikipedia_link=row[WIKIPEDIA_LINK],
        keywords=row[KEYWORDS],
        # INT
        latitude_deg=row[LATITUDE_DEG] or 0,
        longitude_deg=row[LONGITUDE_DEG] or 0,
        elevation_ft=row[ELEVATION_FT] or 0,
        scheduled_service=scheduled_service or False
    )
