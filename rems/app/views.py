from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Property, CustomerMessage, SellRequest, UploadedImage
from django.views.generic import DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

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
    paginator = Paginator(properties, 9)  # Show 9 properties per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "buy.html", context)


def rentpage(request):
    properties = Property.objects.filter(property_for="Renter")
    paginator = Paginator(properties, 9)  # Show 9 properties per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "rent.html", context)


def contactpage(request):
    return render(request, "contact.html")


def sellpage(request):
    if request.method == "POST":
        # Retrieve form field values
        property_title = request.POST.get("property-title")
        property_type = request.POST.get("property-type")
        property_for = request.POST.get("property-for")
        flat_number = request.POST.get("flat-number")
        bedrooms = request.POST.get("bed-number")
        bathrooms = request.POST.get("bath-number")
        living_rooms = request.POST.get("living-number")
        kitchens = request.POST.get("kitchen-number")
        total_rooms = request.POST.get("total-number")
        parking = request.POST.get("parking")
        built_year = request.POST.get("built-year")
        built_area = request.POST.get("built-area")
        road_size = request.POST.get("road-size")
        land_area = request.POST.get("land-area")
        type = request.POST.get("type")
        facing_direction = request.POST.get("facing-direction")
        price = request.POST.get("price")
        price_per_unit = request.POST.get("price-per-unit")
        full_description = request.POST.get("description")
        province = request.POST.get("province")
        district = request.POST.get("district")
        municipality = request.POST.get("municipality")
        ward_no = request.POST.get("ward-no")
        tole = request.POST.get("tole")
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone")
        images = request.FILES.getlist("file")

        if property_type == "Land":
            sell_request = SellRequest(
                property_title=property_title,
                property_type=property_type,
                property_for=property_for,
                flat_number=flat_number,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                living_rooms=living_rooms,
                kitchens=kitchens,
                total_rooms=total_rooms,
                parking=parking,
                built_year=built_year,
                built_area=built_area,
                road_size=road_size,
                land_area=land_area,
                type=type,
                facing_direction=facing_direction,
                price=price,
                price_per_unit=price_per_unit,
                full_description=full_description,
                province=province,
                district=district,
                municipality=municipality,
                ward_no=ward_no,
                tole=tole,
                name=name,
                email=email,
                address=address,
                phone_number=phone_number,
            )
            sell_request.save()
        else:
            sell_request = SellRequest(
                property_title=property_title,
                property_type=property_type,
                property_for=property_for,
                road_size=road_size,
                land_area=land_area,
                type=type,
                facing_direction=facing_direction,
                price=price,
                price_per_unit=price_per_unit,
                full_description=full_description,
                province=province,
                district=district,
                municipality=municipality,
                ward_no=ward_no,
                tole=tole,
                name=name,
                email=email,
                address=address,
                phone_number=phone_number,
            )
            sell_request.save()

        for image in images:
            uploaded_image = UploadedImage(sell_request=sell_request, image=image)
            uploaded_image.save()
        success_message = "Details Uploaded successfully."
        messages.success(request, success_message)
        return redirect("sell")

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
        context = {"property": property, "sucess": sucess}
        return render(request, self.template_name, context)


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


def custom_404_view(request, exception):
    return render(request, "404/404.html", status=404)
