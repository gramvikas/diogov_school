from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.indent, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("manage", views.contact, name='manage'), 
    path("admission", views.index, name='admissions'),
    path("gallery",views.gal,name='gallery'),
    path("activities",views.activ,name='activities'),
    path("LatestNews",views.latest,name='LatestNews'),
    path("infrastructure",views.infra,name='infrastructure'),
]
