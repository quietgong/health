from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.intro, name='intro'),
    path('admin/', admin.site.urls),

    path('community/', include('community.urls')),
    path('workout/', include('workout.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
