from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('aboutus/',views.aboutus),
    path('contact/',views.contact),
    path('create/',views.create),
    
    ]