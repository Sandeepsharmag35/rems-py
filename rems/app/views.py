from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Property, CustomerMessage
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
    properties = Property.objects.filter(property_for="buyer")
    return render(request, "buy.html", {"properties": properties})


def contactpage(request):
    return render(request, "contact.html")


def rentpage(request):
    properties = Property.objects.filter(property_for="renter")
    return render(request, "rent.html", {"for_rent": properties})


def sellpage(request):
    return render(request, "sell.html", {"user": request.user})


class propertyDetailsPage(DetailView):
    template_name = "property-details.html"

    def get(self, request, model, pk):
        if model == "buy":
            property = get_object_or_404(Property, pk=pk)
        elif model == "rent":
            property = get_object_or_404(Property, pk=pk)

        return render(request, self.template_name, {"property": property})

    def post(self, request, model, pk):
        if model == "buy":
            property = get_object_or_404(Property, pk=pk)
        elif model == "rent":
            property = get_object_or_404(Property, pk=pk)

        # Process the form data
        full_name = request.POST.get("full_name")
        email = request.POST.get("email_address")
        phone = request.POST.get("phone_number")
        message = request.POST.get("message")

        inquiry = CustomerMessage(
            #  property=property,
            fullname=full_name,
            email=email,
            phone_number=phone,
            message=message,
        )
        # saving the instance to the database
        inquiry.save()
        sucess = "Message sent Sucessfully."

        return render(
            request, self.template_name, {"property": property, "sucess": sucess}
        )
