from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'about.html')