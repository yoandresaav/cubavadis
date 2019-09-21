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



#link


"""
[14/Sep/2019 20:29:58] "POST /es/panagea/ HTTP/1.1" 302 0
{"SessionKey":"7d7a3593-33dc-44e6-96e3-a3f89d40c8de",
"Query":
    {"Country":"ES","Currency":"EUR","Locale":"es-ES","Adults":1,"Children":0,"Infants":0,"OriginPlace":"13870","DestinationPlace":"3105","OutboundDate":"2019-11-01","LocationSchema":"Default","CabinClass":"economy","GroupPricing":false
    },"Status":"UpdatesPending",
    "Itineraries":[
        {"OutboundLegId":"13870-1911012025--32132-1-12079-1911021815",
            "PricingOptions":[{"Agents":[3051889],"QuoteAgeInMinutes":30,"Price":1116.41,"DeeplinkUrl":"http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=NqagL4PVt5peZGMG189S4zg4dm39CEoR%2bV8UrnEXQEuJZ36mI8cG9Fi4G8qRAMyN&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fES%2fes-ES%2fEUR%2fklm1%2f1%2f13870.12079.2019-11-01%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32132%7c1706%7c13870%7c2019-11-01T20%3a25%7c9451%7c2019-11-01T23%3a00%7c155%7cHLSRWES%7cH%7c-%3bflight%7c-32132%7c723%7c9451%7c2019-11-02T12%3a35%7c12079%7c2019-11-02T18%3a15%7c640%7cHLSRWES%7cH%7c-%26carriers%3d-32132%26operators%3d-32132%3b-32132%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d1116.41%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26q_ids%3dklm1.13870.12079.191101..1..E%7c5623584449236150046%26q_sources%3dJACQUARD%26commercial_filters%3dfalse%26q_datetime_utc%3d2019-09-14T20%3a00%3a00%26pqid%3dfalse"}],
            "BookingDetailsLink":{"Uri":"/apiservices/pricing/v1.0/7d7a3593-33dc-44e6-96e3-a3f89d40c8de/booking","Body":"OutboundLegId=13870-1911012025--32132-1-12079-1911021815&InboundLegId=","Method":"PUT"}},
            
            {"OutboundLegId":"13870-1911010715--32677-1-12079-1911011935",
            
            "PricingOptions":[{"Agents":[1939318],"QuoteAgeInMinutes":1,"Price":1420.53,"DeeplinkUrl":"http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=NqagL4PVt5peZGMG189S4zg4dm39CEoR%2bV8UrnEXQEuJZ36mI8cG9Fi4G8qRAMyN&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fES%2fes-ES%2fEUR%2fairf%2f1%2f13870.12079.2019-11-01%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32677%7c4789%7c13870%7c2019-11-01T07%3a15%7c15083%7c2019-11-01T09%3a15%7c120%7cMFFWES%7cM%7c-%3bflight%7c-32677%7c820%7c10413%7c2019-11-01T14%3a10%7c12079%7c2019-11-01T19%3a35%7c625%7cMFFWES%7cM%7c-%26carriers%3d-32677%26operators%3d-32680%3b-32677%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d1420.53%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26q_ids%3dairf.13870.12079.191101..1..E%7c-5017852464034044247%26q_sources%3dJACQUARD%26commercial_filters%3dfalse%26q_datetime_utc%3d2019-09-14T20%3a29%3a00%26pqid%3dfalse"}],"BookingDetailsLink":{"Uri":"/apiservices/pricing/v1.0/7d7a3593-33dc-44e6-96e3-a3f89d40c8de/booking","Body":"OutboundLegId=13870-1911010715--32677-1-12079-1911011935&InboundLegId=","Method":"PUT"}},{"OutboundLegId":"13870-1911010955--32677-1-12079-1911011935","PricingOptions":[{"Agents":[1939318],"QuoteAgeInMinutes":1,"Price":1245.53,"DeeplinkUrl":"http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=NqagL4PVt5peZGMG189S4zg4dm39CEoR%2bV8UrnEXQEuJZ36mI8cG9Fi4G8qRAMyN&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fES%2fes-ES%2fEUR%2fairf%2f1%2f13870.12079.2019-11-01%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32677%7c1001%7c13870%7c2019-11-01T09%3a55%7c10413%7c2019-11-01T12%3a05%7c130%7cKLSRWES%7cK%7c-%3bflight%7c-32677%7c820%7c10413%7c2019-11-01T14%3a10%7c12079%7c2019-11-01T19%3a35%7c625%7cKLSRWES%7cK%7c-%26carriers%3d-32677%26operators%3d-32677%3b-32677%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d1245.53%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26q_ids%3dairf.13870.12079.191101..1..E%7c-5179733496790205438%26q_sources%3dJACQUARD%26commercial_filters%3dfalse%26q_datetime_utc%3d2019-09-14T20%3a29%3a00%26pqid%3dfalse"}],"BookingDetailsLink":{"Uri":"/apiservices/pricing/v1.0/7d7a3593-33dc-44e6-96e3-a3f89d40c8de/booking","Body":"OutboundLegId=13870-1911010955--32677-1-12079-1911011935&InboundLegId=","Method":"PUT"}},{"OutboundLegId":"13870-1911010640--32677-1-12079-1911011935","PricingOptions":[{"Agents":[1939318],"QuoteAgeInMinutes":1,"Price":1245.53,"DeeplinkUrl":"http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=NqagL4PVt5peZGMG189S4zg4dm39CEoR%2bV8UrnEXQEuJZ36mI8cG9Fi4G8qRAMyN&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fES%2fes-ES%2fEUR%2fairf%2f1%2f13870.12079.2019-11-01%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32677%7c1401%7c13870%7c2019-11-01T06%3a40%7c10413%7c2019-11-01T08%3a55%7c135%7cKLSRWES%7cK%7c-%3bflight%7c-32677%7c820%7c10413%7c2019-11-01T14%3a10%7c12079%7c2019-11-01T19%3a35%7c625%7cKLSRWES%7cK%7c-%26carriers%3d-32677%26operators%3d-32677%3b-32677%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d1245.53%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26q_ids%3dairf.13870.12079.191101..1..E%7c-5076024015508993741%26q_sources%3dJACQUARD%26commercial_filters%3dfalse%26q_datetime_utc%3d2019-09-14T20%3a29%3a00%26pqid%3dfalse"}],"BookingDetailsLink":{"Uri":"/apiservices/pricing/v1.0/7d7a3593-33dc-44e6-96e3-a3f89d40c8de/booking","Body":"OutboundLegId=13870-1911010640--32677-1-12079-1911011935&InboundLegId=","Method":"PUT"}},{"OutboundLegId":"13870-1911011535--32680-0-12079-1911011945","PricingOptions":[{"Agents":[2388174],"QuoteAgeInMinutes":377,"Price":1002.62,"DeeplinkUrl":"http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=NqagL4PVt5peZGMG189S4zg4dm39CEoR%2bV8UrnEXQEuJZ36mI8cG9Fi4G8qRAMyN&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fES%2fes-ES%2fEUR%2felin%2f1%2f13870.12079.2019-11-01%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32680%7c51%7c13870%7c2019-11-01T15%3a35%7c12079%7c2019-11-01T19%3a45%7c550%7cELYO6L%7cE%7cTURISTA+ECONOMY%26carriers%3d-32680%26operators%3d-32680%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d1002.62%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26q_ids%3delin.13870.12079.191101..1..E%7c-3461402163483473823%26q_sources%3dJACQUARD%26commercial_filters%3dfalse%26q_datetime_utc%3d2019-09-14T14%3a13%3a00%26source_website_id%3damae%26pqid%3dfalse"}],"BookingDetailsLink":{"Uri":"/apiservices/pricing/v1.0/7d7a3593-33dc-44e6-96e3-a3f89d40c8de/booking","Body":"OutboundLegId=13870-1911011535--32680-0-12079-1911011945&InboundLegId=","Method":"PUT"}},{"OutboundLegId":"13870-1911011655--32222-0-12079-1911012225","PricingOptions":[{"Agents":[2807314],"QuoteAgeInMinutes":377,"Price":630.62,"DeeplinkUrl":"http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=NqagL4PVt5peZGMG189S4zg4dm39CEoR%2bV8UrnEXQEuJZ36mI8cG9Fi4G8qRAMyN&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fES%2fes-ES%2fEUR%2fiber%2f1%2f13870.12079.2019-11-01%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32222%7c6621%7c13870%7c2019-11-01T16%3a55%7c12079%7c2019-11-01T22%3a25%7c630%7cLNL0NOB6%7cL%7c-%26carriers%3d-32222%26operators%3d-32222%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d630.62%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26q_ids%3diber.13870.12079.191101..1..E%7c-5612475702500753748%26q_sources%3dJACQUARD%26commercial_filters%3dfalse%26q_datetime_utc%3d2019-09-14T14%3a13%3a00%26pqid%3dfalse"}],"BookingDetailsLink":{"Uri":"/apiservices/pricing/v1.0/7d7a3593-33dc-44e6-96e3-a3f89d40c8de/booking","Body":"OutboundLegId=13870-1911011655--32222-0-12079-1911012225&InboundLegId=","Method":"PUT"}}],
            
            "Legs":[{"Id":"13870-1911012025--32132-1-12079-1911021815","SegmentIds":[0,1],"OriginStation":13870,"DestinationStation":12079,"Departure":"2019-11-01T20:25:00","Arrival":"2019-11-02T18:15:00","Duration":1610,"JourneyMode":"Flight","Stops":[9451],"Carriers":[1324],"OperatingCarriers":[1324],"Directionality":"Outbound","FlightNumbers":[{"FlightNumber":"1706","CarrierId":1324},{"FlightNumber":"723","CarrierId":1324}]},{"Id":"13870-1911010715--32677-1-12079-1911011935","SegmentIds":[2,3],"OriginStation":13870,"DestinationStation":12079,"Departure":"2019-11-01T07:15:00","Arrival":"2019-11-01T19:35:00","Duration":1040,"JourneyMode":"Flight","Stops":[15083,10413],"Carriers":[838],"OperatingCarriers":[1816,838],"Directionality":"Outbound","FlightNumbers":[{"FlightNumber":"4789","CarrierId":838},{"FlightNumber":"820","CarrierId":838}]},{"Id":"13870-1911010955--32677-1-12079-1911011935","SegmentIds":[4,3],"OriginStation":13870,"DestinationStation":12079,"Departure":"2019-11-01T09:55:00","Arrival":"2019-11-01T19:35:00","Duration":880,"JourneyMode":"Flight","Stops":[10413],"Carriers":[838],"OperatingCarriers":[838],"Directionality":"Outbound","FlightNumbers":[{"FlightNumber":"820","CarrierId":838},{"FlightNumber":"1001","CarrierId":838}]},{"Id":"13870-1911010640--32677-1-12079-1911011935","SegmentIds":[5,3],"OriginStation":13870,"DestinationStation":12079,"Departure":"2019-11-01T06:40:00","Arrival":"2019-11-01T19:35:00","Duration":1075,"JourneyMode":"Flight","Stops":[10413],"Carriers":[838],"OperatingCarriers":[838],"Directionality":"Outbound","FlightNumbers":[{"FlightNumber":"820","CarrierId":838},{"FlightNumber":"1401","CarrierId":838}]},{"Id":"13870-1911011535--32680-0-12079-1911011945","SegmentIds":[6],"OriginStation":13870,"DestinationStation":12079,"Departure":"2019-11-01T15:35:00","Arrival":"2019-11-01T19:45:00","Duration":550,"JourneyMode":"Flight","Stops":[],"Carriers":[1816],"OperatingCarriers":[1816],"Directionality":"Outbound","FlightNumbers":[{"FlightNumber":"51","CarrierId":1816}]},{"Id":"13870-1911011655--32222-0-12079-1911012225","SegmentIds":[7],"OriginStation":13870,"DestinationStation":12079,"Departure":"2019-11-01T16:55:00","Arrival":"2019-11-01T22:25:00","Duration":630,"JourneyMode":"Flight","Stops":[],"Carriers":[1218],"OperatingCarriers":[1218],"Directionality":"Outbound","FlightNumbers":[{"FlightNumber":"6621","CarrierId":1218}]}],"Segments":[{"Id":0,"OriginStation":13870,"DestinationStation":9451,"DepartureDateTime":"2019-11-01T20:25:00","ArrivalDateTime":"2019-11-01T23:00:00","Carrier":1324,"OperatingCarrier":1324,"Duration":155,"FlightNumber":"1706","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":1,"OriginStation":9451,"DestinationStation":12079,"DepartureDateTime":"2019-11-02T12:35:00","ArrivalDateTime":"2019-11-02T18:15:00","Carrier":1324,"OperatingCarrier":1324,"Duration":640,"FlightNumber":"723","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":2,"OriginStation":13870,"DestinationStation":15083,"DepartureDateTime":"2019-11-01T07:15:00","ArrivalDateTime":"2019-11-01T09:15:00","Carrier":838,"OperatingCarrier":1816,"Duration":120,"FlightNumber":"4789","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":3,"OriginStation":10413,"DestinationStation":12079,"DepartureDateTime":"2019-11-01T14:10:00","ArrivalDateTime":"2019-11-01T19:35:00","Carrier":838,"OperatingCarrier":838,"Duration":625,"FlightNumber":"820","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":4,"OriginStation":13870,"DestinationStation":10413,"DepartureDateTime":"2019-11-01T09:55:00","ArrivalDateTime":"2019-11-01T12:05:00","Carrier":838,"OperatingCarrier":838,"Duration":130,"FlightNumber":"1001","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":5,"OriginStation":13870,"DestinationStation":10413,"DepartureDateTime":"2019-11-01T06:40:00","ArrivalDateTime":"2019-11-01T08:55:00","Carrier":838,"OperatingCarrier":838,"Duration":135,"FlightNumber":"1401","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":6,"OriginStation":13870,"DestinationStation":12079,"DepartureDateTime":"2019-11-01T15:35:00","ArrivalDateTime":"2019-11-01T19:45:00","Carrier":1816,"OperatingCarrier":1816,"Duration":550,"FlightNumber":"51","JourneyMode":"Flight","Directionality":"Outbound"},{"Id":7,"OriginStation":13870,"DestinationStation":12079,"DepartureDateTime":"2019-11-01T16:55:00","ArrivalDateTime":"2019-11-01T22:25:00","Carrier":1218,"OperatingCarrier":1218,"Duration":630,"FlightNumber":"6621","JourneyMode":"Flight","Directionality":"Outbound"}],
            
            "Carriers":[
                {"Id":1324,"Code":"KL","Name":"KLM","ImageUrl":"https://s1.apideeplink.com/images/airlines/KL.png","DisplayCode":"KL"},
                {"Id":1816,"Code":"UX","Name":"Air Europa","ImageUrl":"https://s1.apideeplink.com/images/airlines/UX.png","DisplayCode":"UX"},
                {"Id":838,"Code":"AF","Name":"Air France","ImageUrl":"https://s1.apideeplink.com/images/airlines/AF.png","DisplayCode":"AF"},
                {"Id":1218,"Code":"IB","Name":"Iberia","ImageUrl":"https://s1.apideeplink.com/images/airlines/IB.png","DisplayCode":"IB"}],
            "Agents":[{"Id":2627446,"Name":"GotoGate","ImageUrl":"https://s1.apideeplink.com/images/websites/gtbf.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":3051889,"Name":"KLM","ImageUrl":"https://s1.apideeplink.com/images/websites/klm1.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"Airline"},{"Id":2489155,"Name":"Flyhacks","ImageUrl":"https://s1.apideeplink.com/images/websites/fhac.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2369555,"Name":"eDreams","ImageUrl":"https://s1.apideeplink.com/images/websites/edes.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2141873,"Name":"Air Canada","ImageUrl":"https://s1.apideeplink.com/images/websites/cana.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"Airline"},{"Id":4068219,"Name":"Turkish Airlines","ImageUrl":"https://s1.apideeplink.com/images/websites/turk.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"Airline"},{"Id":4498451,"Name":"Expedia","ImageUrl":"https://s1.apideeplink.com/images/websites/xpes.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":1968846,"Name":"Avianca","ImageUrl":"https://s1.apideeplink.com/images/websites/avin.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"Airline"},{"Id":3588371,"Name":"Tripair","ImageUrl":"https://s1.apideeplink.com/images/websites/pees.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":4035342,"Name":"Travelgenio","ImageUrl":"https://s1.apideeplink.com/images/websites/tgen.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2499060,"Name":"Aeroflot","ImageUrl":"https://s1.apideeplink.com/images/websites/flot.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"Airline"},{"Id":2807314,"Name":"Iberia","ImageUrl":"https://s1.apideeplink.com/images/websites/iber.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"Airline"},{"Id":3934928,"Name":"Kiwi.com","ImageUrl":"https://s1.apideeplink.com/images/websites/skyp.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":3164435,"Name":"lastminute.com","ImageUrl":"https://s1.apideeplink.com/images/websites/lmes.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":1891970,"Name":"Rumbo","ImageUrl":"https://s1.apideeplink.com/images/websites/a582.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":3503123,"Name":"Opodo","ImageUrl":"https://s1.apideeplink.com/images/websites/opes.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2388174,"Name":"Air Europa","ImageUrl":"https://s1.apideeplink.com/images/websites/elin.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"Airline"},{"Id":4251817,"Name":"Viajes El Corte Ingles","ImageUrl":"https://s1.apideeplink.com/images/websites/veci.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":1963108,"Name":"Mytrip","ImageUrl":"https://s1.apideeplink.com/images/websites/at24.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":4074515,"Name":"Tix.es","ImageUrl":"https://s1.apideeplink.com/images/websites/txes.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2491667,"Name":"Flightfinder","ImageUrl":"https://s1.apideeplink.com/images/websites/fies.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":1939318,"Name":"Air France","ImageUrl":"https://s1.apideeplink.com/images/websites/airf.png","Status":"UpdatesComplete","OptimisedForMobile":true,"Type":"Airline"},{"Id":3986805,"Name":"Travel2Be","ImageUrl":"https://s1.apideeplink.com/images/websites/t2be.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2174132,"Name":"Condor","ImageUrl":"https://s1.apideeplink.com/images/websites/cond.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"Airline"},{"Id":4033043,"Name":"Travelfrom.es","ImageUrl":"https://s1.apideeplink.com/images/websites/tfes.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":4132306,"Name":"United","ImageUrl":"https://s1.apideeplink.com/images/websites/uair.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"Airline"},{"Id":1964051,"Name":"Budgetair.es","ImageUrl":"https://s1.apideeplink.com/images/websites/ates.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"},{"Id":2185235,"Name":"Trip.com","ImageUrl":"https://s1.apideeplink.com/images/websites/ctes.png","Status":"UpdatesPending","OptimisedForMobile":true,"Type":"TravelAgent"}],"Places":[{"Id":3105,"ParentId":164,"Code":"HAV","Type":"City","Name":"La Habana"},{"Id":164,"Code":"CU","Type":"Country","Name":"Cuba"},{"Id":200,"Code":"ES","Type":"Country","Name":"España"},{"Id":9451,"ParentId":509,"Code":"AMS","Type":"Airport","Name":"Ámsterdam Schiphol"},{"Id":235,"Code":"NL","Type":"Country","Name":"Países Bajos"},{"Id":15083,"ParentId":6073,"Code":"ORY","Type":"Airport","Name":"París Orly"},{"Id":10413,"ParentId":6073,"Code":"CDG","Type":"Airport","Name":"París Charles de Gaulle"},{"Id":13870,"ParentId":4854,"Code":"MAD","Type":"Airport","Name":"Madrid"},{"Id":12079,"ParentId":3105,"Code":"HAV","Type":"Airport","Name":"La Habana"},{"Id":244,"Code":"FR","Type":"Country","Name":"Francia"},{"Id":4854,"ParentId":200,"Code":"MAD","Type":"City","Name":"Madrid"},{"Id":6073,"ParentId":244,"Code":"PAR","Type":"City","Name":"París"},{"Id":509,"ParentId":235,"Code":"AMS","Type":"City","Name":"Ámsterdam"}],"Currencies":[{"Code":"EUR","Symbol":"€","ThousandsSeparator":".","DecimalSeparator":",","SymbolOnLeft":false,"SpaceBetweenAmountAndSymbol":true,"RoundingCoefficient":0,"DecimalDigits":2}]}
"""