from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 오준호입니다. + 안녕하세요 정채은입니다. + 안녕하세요 김선형입니다.")