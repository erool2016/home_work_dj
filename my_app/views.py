from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request)->HttpResponse:

    categories = Categories.objects.all()

    context = {
        'title': 'Home Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }

    return render(request,'index.html',context)

# def index(request)->HttpResponse:
#     return HttpResponse('index about')

def about(request)->HttpResponse:
    context = {
        'title': 'Home  О нас',
        'content': 'О нас',
        'text_on_page': 'Мы лучшие разработчики'
    }

    return render(request, 'about.html', context)

def my_page(request)->HttpResponse:
    pass

