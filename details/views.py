from django.views.generic.edit import FormView
from .forms import AddressForm


class DetailView(FormView):
    form_class = AddressForm
    success_url = 'home'
    template_name = 'details.html'
