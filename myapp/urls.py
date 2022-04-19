from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),

    path('add_in_basket/<str:product_id>/',
         add_in_basket, name='add_in_basket'),

    path('remove_from_basket/<str:product_id>/',
         remove_from_basket, name='remove_from_basket'),

    path('checkout/', checkout, name='checkout')
]
