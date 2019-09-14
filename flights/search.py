import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

"""
    Args:
    * Required
    - country: STRING Ex. US (The currency you want the prices in (3-letter currency code)
    - currency:STRING Ex. USD (The currency you want the prices in (3-letter currency code))
    - locale: STRING Ex. en-US (The locale you want the results in (ISO locale))
    - originPlace: STRING Ex. SFO-sky (The origin place (see docs for places))
    - destinationPlace: STRING Ex. LHR-sky (The origin place (see docs for places))
    - outboundDate: STRING Ex. 2019-09-01 (The outbound date. Format “yyyy-mm-dd”)
    - adults: NUMBER Ex 1 (Number of adults (16+ years). Must be between 1 and 8.)

    Optional Parameters
    - inboundDate: STRING Ex. 2019-09-10 (The return date. Format “yyyy-mm-dd”. Use empty string for oneway trip.)
    - cabinClass: STRING (The cabin class. Can be “economy”, “premiumeconomy”, “business”, “first”)
    - children: NUMBER (Number of children (1-16 years). Can be between 0 and 8)
    - infants: NUMBER (Number of infants (under 12 months). Can be between 0 and 8.)
    - includeCarriers: STRING (Only return results from those carriers. Comma-separated list of carrier ids.)
    - excludeCarriers: STRING (Filter out results from those carriers. Comma-separated list of carrier ids.)
    - groupPricing: STRING (If set to true, prices will be obtained for the whole passenger 
                            group and if set to false it will be obtained for one adult. 
                            By default it is set to false.)
"""

API_URL = "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
XRAPID_KEY = "4719112acfmsh528779acb528821p1020c0jsn3036e42ecda7"
LOCALE = 'es-ES'


def create_api_session(**kwargs):
    data = [
        f'country={kwargs.get("country")}',
        f'currency={kwargs.get("currency")}',
        f'locale={LOCALE}',
        f'originPlace={kwargs.get("originPlace")}',
        f'destinationPlace={kwargs.get("destinationPlace")}',
        f'outboundDate={kwargs.get("outboundDate")}',
        f'adults={kwargs.get("adults")}'
    ]
    payload = '&'.join(data)
    # payload = f'inboundDate={}&cabinClass=&children=&infants=&'
    headers = {
        'x-rapidapi-host': API_URL,
        'x-rapidapi-key': XRAPID_KEY,
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print('El code del response es %s' % response.status_code)
    print('El text del response es %s' % response.text)
    if response.status_code == 201:  # 201 Created
        print('ALl ok')
        location = response.headers.get('location')
        rapid_api_host = '/'.join(location.split('/')[:-1]) + '/'
        key = location.split('/')[-1]
        # Guardarla en sessions y la fecha en que se creo
        print('La key es %s' % key)
        return key
    # Other error example 400
    raise Exception(response.text)
"""
http://partners.api.skyscanner.net/apiservices/pricing/uk2/v1.0/c6fdaa87-c11e-4ba6-8ff0-1cfbfd4750ed
len = 36
"""

def get_poll_session_result(key):
    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/{key}"

    querystring = {"pageIndex":"0", "pageSize":"10"}

    headers = {
        'x-rapidapi-host': API_URL,
        'x-rapidapi-key': XRAPID_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    if response.status_code == 200:
        return response.text
    raise Exception(response.text)



def get_place(query='Spain'):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/CU/EUR/es-ES/"
    
    querystring = {
        "query": 'Cuba'
    }
    headers = {
        'x-rapidapi-host': API_URL,
        'x-rapidapi-key': XRAPID_KEY
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring
    )
    """
        Retorna una lista de places
        {
            "PlaceId":"STOC-sky"
            "PlaceName":"Stockholm"
            "CountryId":"SE-sky"
            "RegionId":""
            "CityId":"STOC-sky"
            "CountryName":"Sweden"
        }
    """
    print(response.text)




# Only for utils

def get_list_market():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "4719112acfmsh528779acb528821p1020c0jsn3036e42ecda7"
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)


def get_list_curriencies():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/currencies"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "4719112acfmsh528779acb528821p1020c0jsn3036e42ecda7"
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
