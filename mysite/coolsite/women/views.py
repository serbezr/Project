from django.shortcuts import render

def index(request):
    return HttpResponce("Страница приложения women")


def categories(request,cat):
    return HttpResponce(f"<h1>Статьи по категориям</h><p>{cat}</p>")


def archive(request,year):
    return HttpResponce(f"<h1>Архив по годам</h1><p>{year}</p>")