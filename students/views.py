from django.shortcuts import render
from .models import Dates, Guidelines


def students(request):
    dates = Dates.objects.first()
    guide = Guidelines.objects.all()

    context = {'dates': dates, 'guide': guide}
    return render(request, 'students/students.html', context)


