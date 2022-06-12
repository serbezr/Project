from django.shortcuts import render

def index(request):
    return HttpResponce("Страница приложения women")


def categories(request,catid):
    return HttpResponce(f"<h1>Статьи по категориям</h><p>{catid}</p>")