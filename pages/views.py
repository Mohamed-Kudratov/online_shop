from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from pages.froms import ContactModelForm


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
