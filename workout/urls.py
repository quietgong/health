from django.urls import path

from workout import views

app_name = 'workout'

urlpatterns = [

    path('', views.index, name='index'),

]