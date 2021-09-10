from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generic', views.generic, name='generic'),
]