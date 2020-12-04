from django.http import HttpResponse


def index(request):
    return HttpResponse("우리는 멋쟁이들")