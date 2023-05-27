from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import CustomerMessage, Property, SellRequest
from account.models import Profile
from django.contrib import messages

# Create your views here.


def adminLogin(request):
    if request.method == "POST":
        username = request.POST.get("admin-username")
        password = request.POST.get("admin-password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            error_message = "Your username or password is incorrect."
            return render(
                request, "admin/admin-login.html", {"error_message": error_message}
            )
    return render(request, "admin/admin-login.html")


def adminLogout(request):
    logout(request)
    return redirect("admin_login")


@login_required(login_url=login)
def AdminDashboard(request):
    context = {"user": request.user}
    return render(request, "admin/dashboard.html", context)


@login_required(login_url=login)
def customerMessage(request):
    messages = CustomerMessage.objects.select_related("property")
    context = {"message": messages}
    return render(request, "admin/message.html", context)


@login_required(login_url=login)
def Delete_CustomerMessage(request, msg_id):
    try:
        msg = CustomerMessage.objects.get(id=msg_id)
        msg.delete()
        messages.success(request, f"The message has been deleted successfully.")
    except CustomerMessage.DoesNotExist:
        messages.error(request, "The message does not exist.")
    return redirect("messages")


@login_required(login_url=login)
def Customers(request):
    profile = Profile.objects.filter(user__is_superuser=False)
    context = {"profile": profile}
    return render(request, "admin/customers.html", context)


@login_required(login_url=login)
def Update_Customer(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    user = profile.user
    username = user.username

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone")

        # Update the user's profile
        profile.fullname = full_name
        profile.email = email
        profile.phone_number = phone_number
        profile.save()
        messages.success(
            request, f"The user @'{username}''s profile has been updated successfully."
        )

        return redirect("customers")
    context = {"profile": profile}
    return render(request, "admin/customers.html", context)


@login_required(login_url=login)
def Delete_Customer(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        user = profile.user
        username = user.username
        user.delete()
        messages.success(
            request, f"The user @'{username}' has been deleted successfully."
        )
    except Profile.DoesNotExist:
        messages.error(request, "The user profile does not exist.")
    return redirect("customers")


@login_required(login_url=login)
def Admins(request):
    profile = Profile.objects.filter(user__is_superuser=True)
    context = {"profile": profile}
    return render(request, "admin/admins.html", context)


def Remove_Admin(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        user = profile.user
        username = user.username
    except Profile.DoesNotExist:
        messages.error(request, "The user profile does not exist.")

    if user.is_superuser or user.is_staff:
        user.is_superuser = False
        user.is_staff = False
        user.save()
        messages.success(
            request, f"'{username}' has been removed as 'admin' successfully."
        )
    else:
        messages.error(request, f"'{username}' is not an admin.")

    return redirect("admins")


@login_required(login_url=login)
def PropertyList(request):
    properties = Property.objects.all()
    context = {"properties": properties}
    return render(request, "admin/properties.html", context)


@login_required(login_url=login)
def AddProperty(request):
    if request.method == "POST":
        property_type = request.POST.get("property-type")
        property_for = request.POST.get("property-for")
        image = request.POST.get("property-image")
        price = request.POST.get("property-price")
        city = request.POST.get("city")
        district = request.POST.get("district")
        zip_code = request.POST.get("zip-code")
        description = request.POST.get("description")
        status = request.POST.get("status")

        property = Property(
            property_type=property_type,
            property_for=property_for,
            image=image,
            price=price,
            city=city,
            district=district,
            zip_code=zip_code,
            description=description,
            status=status,
        )
        property.save()
        messages.success(request, f"Property has been added successfully.")
        return redirect("add-property")

    return render(request, "admin/add_property.html")


def SellRequest(request):
    if request.method == "POST":
        property_title = request.POST.get("property-title")
        property_type = request.POST.get("property-title")
        property_for = request.POST.get("property-title")
        flat_number = request.POST.get("property-title")
        bedrooms = request.POST.get("property-title")
        bathrooms = request.POST.get("property-title")
        living_rooms = request.POST.get("property-title")
        kitchens = request.POST.get("property-title")
        total_rooms = request.POST.get("property-title")
        parking = request.POST.get("property-title")
        built_year = request.POST.get("property-title")
        built_area = request.POST.get("property-title")
        road_size = request.POST.get("property-title")
        land_area = request.POST.get("property-title")
        type = request.POST.get("property-title")
        facing_direction = request.POST.get("property-title")
        price = request.POST.get("property-title")
        price_per_unit = request.POST.get("property-title")
        full_description = request.POST.get("property-title")
        province = request.POST.get("property-title")
        district = request.POST.get("property-title")
        municipality = request.POST.get("property-title")
        ward_no = request.POST.get("property-title")
        tole = request.POST.get("property-title")
        name = request.POST.get("property-title")
        email = request.POST.get("property-title")
        address = request.POST.get("property-title")
        phone_number = request.POST.get("property-title")
        image = request.FILES.getlist("property-title")

        if property_type == "Land":
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
                image=image,
            )

    return render(request, "admin/sellrequest.html")
