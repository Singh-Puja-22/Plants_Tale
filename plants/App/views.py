from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.models import Plant

# Create your views here.
def Home(request):
    return HttpResponse("Hello")

class PlantList(ListView):
    queryset = Plant.objects.all()

class PlantDetail(DetailView):
    queryset = Plant.objects.all()
    template_name = "plant_detail.html"