from django.shortcuts import render

from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Это страница главная страница")

def news(request):
    return HttpResponse("Это страница Новости")

def program(request):
    return HttpResponse("Это страница ПРОГРАММА ИЗУЧЕНИЯ АМУРСКОГО ТИГРА НА РОССИЙСКОМ ДАЛЬНЕМ ВОСТОКЕ")

def animal(request):
    return HttpResponse("Это страница О Жизни АМУРСКОГО ТИГРА")

def history(request):
    return HttpResponse('Это страница ИСТОРИЯ ИЗУЧЕНИЯ')

def premier(request):
    return HttpResponse('Это страница ВИЗИТ ПУТИНА')

def photos(request):
    return HttpResponse('Это страница МУЛЬТИМЕДИЯ')

