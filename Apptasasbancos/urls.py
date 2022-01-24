from unicodedata import name
from django.urls import path
from dataclasses import dataclass
from django.shortcuts import render

from Apptasasbancos import views


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('bancos/', views.bancos, name= 'bancos'),
    path('productos/', views.productos, name= 'productos'),
    path('tasas/', views.tasas, name= 'tasas'),
]
