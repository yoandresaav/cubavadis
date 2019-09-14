from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseForbidden,
    JsonResponse,
)

from flights.search import create_api_session, get_poll_session_result
from flights.models import Places

from .handlers import handle_session_sky


def send_form_vuelos(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            handle_session_sky(request.POST)
            manejador_eventos(request, **kwargs)
        except Exception as e:
            return HttpResponseForbidden()
    return JsonResponse({})
    #'dates': ['09-11-19 > 10-23-19'], 'qtyInput': ['3', '0']}


def manejador_eventos(request, **kwargs):
    key = request.session.get('key_vuelo')
    if not key:
        key = create_api_session(**kwargs)
        request.session['key_vuelo'] = key
    return key


def retornador_respuesta_vuelos(request):
    key = request.session.get('key_vuelo')
    if not key:
        return HttpResponseForbidden
    result = get_poll_session_result(key)
    return JsonResponse({'data': result})
