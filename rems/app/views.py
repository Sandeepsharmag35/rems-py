from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Property, RentProperty
from django.views.generic import DetailView


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
    return render(request, "buy.html", {"properties": properties})


def contactpage(request):
    return render(request, "contact.html")


def rentpage(request):
    rentproperties = RentProperty.objects.all()
    return render(request, "rent.html", {"for_rent": rentproperties})


def sellpage(request):
    return render(request, "sell.html", {"user": request.user})


# def propertyDetailsPage(request, property_id):
#     property = get_object_or_404(Property, id=property_id)
#     return render(request, "property-details.html", {"property": property})


class propertyDetailsPage(DetailView):
    template_name = "property-details.html"

    def get(self, request, model, pk):
        if model == "buy":
            property = get_object_or_404(Property, pk=pk)
        elif model == "rent":
            property = get_object_or_404(RentProperty, pk=pk)

        return render(request, self.template_name, {"property": property})
