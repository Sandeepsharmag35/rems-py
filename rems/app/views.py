from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Property, CustomerMessage
from django.views.generic import DetailView
from django.db.models import Q

# Create your views here.


def aboutpage(request):
    return render(request, "about.html")


def agentspage(request):
    return render(request, "agents.html")


def blogpage(request):
    return render(request, "blog.html")


def blogdetailspage(request):
    return render(request, "blogdetail.html")


def buypage(request):
    properties = Property.objects.filter(property_for="Buyer")
    return render(request, "buy.html", {"properties": properties})


def contactpage(request):
    return render(request, "contact.html")


def rentpage(request):
    properties = Property.objects.filter(property_for="Renter")
    return render(request, "rent.html", {"properties": properties})


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
            property=property,
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


def SearchResultPage(request):
    location = request.GET.get("location", "")
    property_for = request.GET.get("property_for", "")
    property_type = request.GET.get("property_type", "")
    #   price_range = request.GET.get("price_range", "")

    properties = Property.objects.all()

    if location:
        properties = properties.filter(
            Q(city__icontains=location) | Q(district__icontains=location)
        )

    if property_for:
        properties = properties.filter(property_for__icontains=property_for)

    if property_type:
        properties = properties.filter(property_type__icontains=property_type)

    # if price_range:
    #     price_ranges = price_range.split("-")
    #     min_price = price_ranges[0].strip()
    #     max_price = price_ranges[1].strip() if len(price_ranges) > 1 else None

    #     if max_price:
    #         properties = properties.filter(price__gte=min_price, price__lte=max_price)
    #     else:
    #         properties = properties.filter(price__gte=min_price)

    context = {"properties": properties}
    return render(request, "search/search-result.html", context)
