from django.shortcuts import render
from .models import House
# Create your views here.

def housing(request):
    house = House.objects.all()
    context = {'house': house}
    return render(request, 'housing/housing.html', context)
