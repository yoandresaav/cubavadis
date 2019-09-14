from datetime import datetime

from flights.models import Places

"""
if not origen or not destino or not dates or not pasajeros:
            return HttpResponseBadRequest()
"""


def handle_session_sky(data):
    # lugares
        origen = data.get('autocomplete-origen')
        destino = data.get('autocomplete-destino')

        # fechas
        dates = data.get('dates')
        pasajeros = data.getlist('qtyInput')
        if not origen or not destino or not dates or not pasajeros:
            raise Exception('Datos incompletos')

        origen = Places.objects.filter(place_name=origen).first().place_id
        destino = Places.objects.filter(place_name=destino).first().place_id
        # get dates
        dates = dates.split('>')
        print('la fecha es **%s**' % dates[0])
        objInicio = datetime.strptime(dates[0].strip(), '%m-%d-%y')
        date_inicio = objInicio.strftime('%Y-%m-%d')

        objFinal = datetime.strptime(dates[1].strip(), '%m-%d-%y')
        date_final = objFinal.strftime('%Y-%m-%d')
        # get pasajeros
        adultos = pasajeros[0]
        boys = pasajeros[1]

        print('Origen %s, Destino %s, inicio %s, final %s, adultos %s, niños %s' % (
            origen, destino, date_inicio, date_final, adultos, boys
        ))
        return {
            'country': 'ES',
            'currency': 'EUR',
            'originPlace': origen,
            'destinationPlace': destino,
            'outboundDate': date_final,
            'adults': adultos
        }