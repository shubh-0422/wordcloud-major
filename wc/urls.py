from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('aboutus/',views.aboutus),
    path('contact/',views.contact),
    
    ]