from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 저는 오준호입니다. ")