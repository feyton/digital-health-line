from django.contrib import admin
from django.urls import path
from .views import about, blog, contact, home, price, service, team

urlpatterns = [
    path('', home),
    path('about', about),
    path('service', service),
    path('team', team),
    path('contact', contact),
    path('price', price),
    path('blog', blog),
]
