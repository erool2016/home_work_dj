from django.http import HttpResponse
from django.shortcuts import render

def index(request)->HttpResponse:
    context = {
        'title': 'Home',
        'content': 'Главная страница моего магазина',
        'list': ['first','second'],
        'dict': {'first': 1},
        'auth': True
    }

    return render(request,'index.html',context)

# def index(request)->HttpResponse:
#     return HttpResponse('index about')

def about(request)->HttpResponse:
    return HttpResponse('Home about')
