from django.urls import path
from .views import about, blog, contact, home, price, service, team

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('service', service),
    path('team', team),
    path('contact', contact),
    path('price', price),
    path('blog', blog, name="blog"),
]
