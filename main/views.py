from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def intro(request):
    return render(request, 'main/about.html')