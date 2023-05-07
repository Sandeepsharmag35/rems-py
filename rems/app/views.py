from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Property, RentProperty


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


def contactpage(request):
    return render(request, "contact.html")


def propertyDetailsPage(request):
    return render(request, "property-detail.html")


def rentpage(request):
    rentproperties = RentProperty.objects.all()
    return render(request, "rent.html", {'for_rent': rentproperties})


def sellpage(request):
    return render(request, "sell.html")