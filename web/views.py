
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'web/index.html'


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
