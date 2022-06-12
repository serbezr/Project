from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Страница приложения women")


def categories(request,caidt):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h><p>{catid}</p>")


def archive(request,year):
    if int(year)>2020:
        raise Http 404
    return HttpResponce(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request,exeption):
    return: HttpResponseNotFound(<h1>Страница не найдена</h1>)

def archive(request,year):
    if int(year)>2020:
        return redirect('/')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def archive(request,years):
    if int(years) <2020:
        return redirect('home', permanent=True)