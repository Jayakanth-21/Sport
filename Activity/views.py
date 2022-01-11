from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Choices


def index(request):
    return HttpResponse("Hello, am creating a sports app")


class HomePageView(TemplateView):

    template_name = "places/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = 'play'
        print(Choices.objects.all())  # Fetches all the records from the database of destination model
        return context

class SportSpecifics(ListView):

    model = Choices
    template_name = 'play/sportspecifics.html'


class CreateUserForm(CreateView):

    model = Choices
    fields = '__all__'
    template_name ='play/userformpage.html'

# Create your views here.
