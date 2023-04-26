from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, "index.html")


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
    return render(request, "buy.html")


def rentpage(request):
    return render(request, "rent.html")


def contactpage(request):
    return render(request, "contact.html")


def propertyDetailsPage(request):
    return render(request, "property-detail.html")


def sellpage(request):
    user = request.user
    return render(request, "sell.html")
