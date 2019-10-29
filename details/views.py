from django.views.generic.edit import FormView
from .forms import DetailsForm


class DetailView(FormView):
    form_class = DetailsForm
    template_name = 'details.html'
    success_url = 'home'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
