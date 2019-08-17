from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    HomeView, ToursView, AboutView, GalleryView,
    BlogView, ContactsView, SearchFlights
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
]
