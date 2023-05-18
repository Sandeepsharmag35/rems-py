from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import CustomerMessage
from account.models import Profile
from app.models import Property
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
    return render(request, "admin/dashboard.html", {"user": request.user})


def customerMessage(request):
    message = CustomerMessage.objects.all()
    return render(request, "admin/message.html", {"message": message})


def Customers(request):
    profile = Profile.objects.filter(user__is_superuser=False)
    return render(request, "admin/customers.html", {"profile": profile})


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

    return render(request, "admin/customers.html", {"profile": profile})


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


def Admins(request):
    profile = Profile.objects.filter(user__is_superuser=True)
    return render(request, "admin/admins.html", {"profile": profile})


def PropertyList(request):
    properties = Property.objects.all()
    context = {"properties": properties}
    return render(request, "admin/properties.html", context)


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
