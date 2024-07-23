from django.shortcuts import render, redirect
from .models import Scrol, Slide, News




def home(request):
    scroll =Scrol.objects.all()
    slide = Slide.objects.filter()
    news = News.objects.all()
    context = {'slide':slide, 'scroll': scroll, 'news': news}
    return render(request, 'home/index.html', context)


