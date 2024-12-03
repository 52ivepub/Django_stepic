from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1>')

def products(requests, id):
    return HttpResponse(f'<h1>Список товаров {id}</h1>')

def new(request, id):
    return HttpResponse(f'<h1>Новые товары {id}</h1>')

def top(request, id):
    return HttpResponse(f'<h1 class=text-center text-uppercase color:red mb-3>Наиболее популярные товары {id}</h1>')
