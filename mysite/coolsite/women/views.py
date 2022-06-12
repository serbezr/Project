from django.shortcuts import render

def index(request):
    return HttpResponce("Страница приложения women")


def categories(request,cat):
    return HttpResponce(f"<h1>Статьи по категориям</h><p>{cat}</p>")