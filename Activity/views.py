from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Choices, PlayerEligibility
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.utils import timezone


def index(request):
    return HttpResponse("Hello, am creating a sports app")


class HomePageView(TemplateView):

    template_name = "Activity/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = 'play'
        print(Choices.objects.all())  # Fetches all the records from the database of destination model
        return context

class SportSpecifics(ListView):

    model = Choices
    template_name = 'Activity/sportspecifics.html'


class PlayerSpecifics(ListView):
    model = PlayerEligibility
    # template_name = 'Activity/sportspecifics.html'


class CreateUserForm(CreateView):

    model = Choices
    fields = '__all__'
    template_name ='Activity/userformpage.html'
    success_url = reverse_lazy('admin page')


class CreatePlayerForm(CreateView):

    model = PlayerEligibility
    fields = '__all__'
    template_name ='Activity/playerdetails.html'
    success_url = reverse_lazy('admin page')

class PlayerDetailView(DetailView):

   model = PlayerEligibility


   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['now'] = timezone.now()
      return context

class PlayerDeletevView(DeleteView):

    model = PlayerEligibility
    success_url = reverse_lazy('sportspecifics')

# Create your views here.
