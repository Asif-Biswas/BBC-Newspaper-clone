from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    top_news = News.objects.filter(category__name = 'Top News').order_by('-id')[:5]
    for i in top_news:
        if len(i.important_part) > 150:
            i.important_part = i.important_part[:100] + '....'

    news = News.objects.filter(category__name = 'News').order_by('-id')[:4]
    for i in news:
        if len(i.important_part) > 150:
            i.important_part = i.important_part[:150] + '....'

    sport = News.objects.filter(category__name = 'Sport').order_by('-id')[:4]
    for i in sport:
        if len(i.important_part) > 150:
            i.important_part = i.important_part[:150] + '....'

    asia = News.objects.filter(category__name = 'Asia News').order_by('-id')[:4]
    for i in asia:
        if len(i.important_part) > 150:
            i.important_part = i.important_part[:150] + '....'

    editors = News.objects.filter(category__name = "Editor's Picks").order_by('-id')[1:4]
    editors0 = News.objects.filter(category__name = "Editor's Picks").order_by('-id')[:1]
    for i in editors:
        if len(i.important_part) > 150:
            i.important_part = i.important_part[:150] + '....'

    reel = News.objects.filter(category__name = 'REEL').order_by('-id')[:3]
    topstories = News.objects.all().order_by('?')[:5]
    return render(request, 'home.html', {
        'top_news': top_news,
        'news': news,
        'sport': sport,
        'reel': reel,
        'asia': asia,
        'editors': editors,
        'editors0': editors0,
        'topstories': topstories,
    })

def news(request, pk):
    news = News.objects.get(id=pk)
    category = news.category.name
    similar = News.objects.filter(category__name = category).exclude(id=pk)[:4]

    topstories = News.objects.all().order_by('?').exclude(id=pk)[:4]
    random = News.objects.all().order_by('?').exclude(id=pk)[:3]
    return render(request, 'news.html', {
        'news': news,
        'similar': similar,
        'topstories': topstories,
        'random': random
    })