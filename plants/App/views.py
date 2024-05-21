from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.models import Plant

# Create your views here.
def Home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

class PlantCreate(CreateView):
    model = Plant
    fields = "__all__"
    template_name = "add_plant.html"
    success_url = '/list'

    
class EditPlant(UpdateView):
    model = Plant
    fields = "__all__"
    template_name = "add_plant.html"
    success_url = '/list'

class DeletePlant(DeleteView):
    model = Plant
    template_name = 'deleteplant.html'
    success_url = '/list'

class PlantList(ListView):
    queryset = Plant.objects.all()

class PlantDetail(DetailView):
    queryset = Plant.objects.all()
    template_name = "plant_detail.html"

def search(request):
    query = request.GET.get('q')
    results = Plant.objects.filter(name__icontains=query)
    template = 'search_result.html'
    context = {
        'results': results,
        'query': query,
    }
    return render(request, template, context)
