from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Property


# Create your views here.

def aboutpage(request):
    return render(request, "about.html")


def agentspage(request):
    return render(request, "agents.html")


def blogpage(request):
    return render(request, "blog.html")


def blogdetailspage(request):
    return render(request, "blogdetail.html")


def buySaleRentPage(request):
    return render(request, "buysalerent.html")


def buypage(request):
    properties = Property.objects.all()
    return render(request, "buy.html",{'properties': properties})


def rentpage(request):
    return render(request, "rent.html")


def contactpage(request):
    return render(request, "contact.html")


def propertyDetailsPage(request):
    return render(request, "property-detail.html")


def sellpage(request):
    return render(request, "sell.html")
