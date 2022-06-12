from django.shortcuts import render

def index(request):
    return HttpResponce("Страница приложения women")


def categories(request,caidt):
    if request.GET:
        print(request.GET)
    return HttpResponce(f"<h1>Статьи по категориям</h><p>{catid}</p>")


def archive(request,year):
    return HttpResponce(f"<h1>Архив по годам</h1><p>{year}</p>")