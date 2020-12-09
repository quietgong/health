from django.shortcuts import render


def index(request):
    return render(request, 'intro.html')


def intro(request):
    return render(request, 'about.html')