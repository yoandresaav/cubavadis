import json
import time

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

from flights.search import create_api_session, get_place, get_poll_session_result

from .handlers import handle_session_sky
from .utils import convert_result_in_template_obj
from .models import Tours

class HomeView(TemplateView):
    template_name = 'panagea/index.html'

    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        
        try:
            data = handle_session_sky(request.POST)
        except:
            data = None
            messages.error(request, "La información proporcionada no es correcta.")
        
        if data:
            try:
                key = create_api_session(**data)
                if key:
                    time.sleep(7)
                    return redirect('web:resultados_vuelos', perfil=key)
            except:
                messages.error(request, "Lo sentimos tenemos un error. Inténtalo otra vez")
        return self.render_to_response(ctx)


class SearchFlights(TemplateView):
    template_name = 'web/search-flights.html'


class ToursView(TemplateView):
    template_name = 'web/tours.html'


class AboutView(TemplateView):
    template_name = 'web/about.html'


class GalleryView(TemplateView):
    template_name = 'web/gallery.html'


class BlogView(TemplateView):
    template_name = 'web/blog.html'


class ContactsView(TemplateView):
    template_name = 'web/contacts.html'


class ResultadosVuelosView(TemplateView):
    template_name = 'panagea/cart-1.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        key = kwargs.get('perfil')
        if key:
            result = get_poll_session_result(key)
            if result:
                itinerarios = convert_result_in_template_obj(result)
                ctx.update({
                    'itinerarios': itinerarios
                })
            return self.render_to_response(ctx)
        else:
            # si no hay key regresa a home
            return redirect('web:home')


class ToursCubaView(TemplateView):
    template_name = 'panagea/tours-cuba.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['tours'] = Tours.objects.all()
        return ctx


class VisadoView(TemplateView):
    template_name = 'panagea/visado.html'
