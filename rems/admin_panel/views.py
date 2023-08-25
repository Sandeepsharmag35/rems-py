from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
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
    total_properties = Property.objects.count()
    total_sell_requests = SellRequest.objects.count()
    total_messages = CustomerMessage.objects.count()
    sell_requests = SellRequest.objects.all()
    inquiries = CustomerMessage.objects.all()
    context = {
        "user": request.user,
        "total_properties": total_properties,
        "total_sell_requests": total_sell_requests,
        "total_messages": total_messages,
        "sell_requests": sell_requests,
        "msg": inquiries,
    }
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
    users = User.objects.all()
    context = {"users": users}
    return render(request, "admin/users.html", context)


@login_required(login_url=login)
def CustomersProfile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(
        user=user, defaults={"fullname": "", "phone_number": "", "email": user.email}
    )
    context = {"profile": profile}
    return render(request, "admin/user_profile.html", context)


@login_required(login_url=login)
def AddUser(request):
    if request.method == "POST":
        email = request.POST["user_email"]
        uname = request.POST["username"]
        pass1 = request.POST["user_password"]

        # Password Validation Process
        try:
            validate_password(pass1)
        except ValidationError as error:
            error = "Your password must contain at least one special character (~!@#$%^&*()_+}{\":?><,./;') and one number."
            messages.error(request, f"'{error}'")
            return render(request, "admin/add_user.html")
        # End Of Validation

        # Username and Email Validation
        if User.objects.filter(username=uname).exists():
            error_message = "Username already taken, try another."
            messages.error(request, f"'{error_message}'")
            return render(request, "admin/add_user.html")

        # Checking if email already exists
        if User.objects.filter(email=email).exists():
            error_message = (
                "Entered Email is already associated with other account, try another"
            )
            messages.error(request, f"'{error_message}'")
            return render(request, "admin/add_user.html")
        # End of Username and Email Validation

        pass2 = request.POST["user_cpassword"]

        if pass1 != pass2:
            error_message = "Your password and confirm password didn't match!"
            return render(request, "admin/add_user.html")

        else:
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()
            messages.success(request, f"User with @'{uname}' Created Sucessfully!")
            return redirect("users")
    return render(request, "admin/add_user.html")


@login_required(login_url=login)
def Update_Customer(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    user = profile.user
    username = user.username

    if request.method == "POST":
        full_name = request.POST.get("full-name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone")
        profile_picture = request.FILES.get("profile-picture")

        # Update the user's profile
        profile.fullname = full_name
        profile.email = email
        profile.phone_number = phone_number
        profile.profile_picture = profile_picture

        profile.save()
        messages.success(
            request, f"The user @'{username}''s profile has been updated successfully."
        )

        return redirect("user-profile", user_id=user.id)
    context = {"profile": profile}
    return render(request, "admin/user_profile.html", context)


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
    return redirect("users")


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
def UpdateProperty(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
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
        price = request.POST.get("property-price")
        price_per_unit = request.POST.get("price-per-unit")
        description = request.POST.get("description")
        province = request.POST.get("province")
        district = request.POST.get("district")
        zip_code = request.POST.get("zip-code")
        city = request.POST.get("city")
        municipality = request.POST.get("municipality")
        ward_no = request.POST.get("ward-no")
        tole = request.POST.get("tole")
        status = request.POST.get("status")
        featured = request.POST.get("featured")
        image_front = request.FILES.get("front-image")
        image_side = request.FILES.get("side-image")
        image_extra1 = request.FILES.get("extra1-image")
        image_extra2 = request.FILES.get("extra2-image")

        property = Property(
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
            full_description=description,
            province=province,
            district=district,
            zip_code=zip_code,
            city=city,
            municipality=municipality,
            ward_no=ward_no,
            tole=tole,
            image_front=image_front,
            image_side=image_side,
            image_extra=image_extra1,
            image_extra2=image_extra2,
            status=status,
            featured=featured,
        )
        property.save()
        messages.success(request, f"Property has been updated successfully.")
        return redirect("update-property")
    context = {"property": property}
    return render(request, "admin/listed_property_details.html", context)


@login_required(login_url=login)
def AddProperty(request):
    if request.method == "POST":
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
        price = request.POST.get("property-price")
        price_per_unit = request.POST.get("price-per-unit")
        description = request.POST.get("description")
        province = request.POST.get("province")
        district = request.POST.get("district")
        zip_code = request.POST.get("zip-code")
        city = request.POST.get("city")
        municipality = request.POST.get("municipality")
        ward_no = request.POST.get("ward-no")
        tole = request.POST.get("tole")
        status = request.POST.get("status")
        featured = request.POST.get("featured")
        image_front = request.FILES.get("front-image")
        image_side = request.FILES.get("side-image")
        image_extra1 = request.FILES.get("extra1-image")
        image_extra2 = request.FILES.get("extra2-image")

        property = Property(
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
            full_description=description,
            province=province,
            district=district,
            zip_code=zip_code,
            city=city,
            municipality=municipality,
            ward_no=ward_no,
            tole=tole,
            image_front=image_front,
            image_side=image_side,
            image_extra=image_extra1,
            image_extra2=image_extra2,
            status=status,
            featured=featured,
        )
        property.save()
        messages.success(request, f"Property has been added successfully.")
        return redirect("add-property")

    return render(request, "admin/add_property.html")


@login_required(login_url=login)
def Sell_Request_List(request):
    sell_requests = SellRequest.objects.all()
    context = {"sell_requests": sell_requests}
    return render(request, "admin/sellrequest.html", context)


@login_required(login_url=login)
def Sell_Request_View(request, sellrequest_id):
    sellrequest = get_object_or_404(SellRequest, id=sellrequest_id)
    if request.method == "POST":
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
        price = request.POST.get("property-price")
        price_per_unit = request.POST.get("price-per-unit")
        description = request.POST.get("description")
        province = request.POST.get("province")
        district = request.POST.get("district")
        zip_code = request.POST.get("zip-code")
        city = request.POST.get("city")
        municipality = request.POST.get("municipality")
        ward_no = request.POST.get("ward-no")
        tole = request.POST.get("tole")
        status = request.POST.get("status")
        featured = request.POST.get("featured", False)

        featured = featured == "on"

        image_front = request.FILES.get("front-image")
        image_side = request.FILES.get("side-image")
        image_extra1 = request.FILES.get("extra1-image")
        image_extra2 = request.FILES.get("extra2-image")

        property = Property.objects.create(
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
            description=description,
            province=province,
            district=district,
            zip_code=zip_code,
            city=city,
            municipality=municipality,
            ward_no=ward_no,
            tole=tole,
            image=image_front,
            image_side=image_side,
            image_extra=image_extra1,
            image_extra2=image_extra2,
            status=status,
            featured=featured,
        )
        messages.success(
            request, f"Request approved and Property has been listed successfully."
        )
        return redirect("sell_request_list")
    context = {"sellrequest": sellrequest}
    return render(request, "admin/sellrequest_view.html", context)


# @login_required(login_url=login)
# def SellRequestDelete(request, sellrequest_id):
#     sellrequest = get_object_or_404(SellRequest, id=sellrequest_id)
#     sellrequest.delete()
#     return render(request, "admin/sellrequest.html")
