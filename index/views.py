from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def team(request):
    return render(request, "team.html")


def contact(request):
    return render(request, "contact.html")


def price(request):
    return render(request, "price.html")


def blog(request):
    return render(request, "blog.html")
