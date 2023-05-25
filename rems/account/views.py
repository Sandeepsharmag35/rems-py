from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib import messages


# Create your views here.


def Indexpage(request):
    return render(request, "index.html")


def RegisterPage(request):
    if request.method == "POST":
        email = request.POST["form_email"]
        uname = request.POST["form_name"]
        pass1 = request.POST["form_password"]

        # Password Validation Process
        try:
            validate_password(pass1)
        except ValidationError as error:
            error = "Your password must contain at least one special character (~!@#$%^&*()_+}{\":?><,./;') and one number."
            return render(request, "register.html", {"error": error})
        # End Of Validation

        # Username and Email Validation
        if User.objects.filter(username=uname).exists():
            error_message = "Username already taken, try another."
            return render(
                request, "register.html", {"error_message_username": error_message}
            )

        # Checking if email already exists
        if User.objects.filter(email=email).exists():
            error_message = (
                "Entered Email is already associated with other account, try another"
            )
            return render(
                request, "register.html", {"error_message_email": error_message}
            )
        # End of Username and Email Validation

        pass2 = request.POST["form_cpassword"]

        if pass1 != pass2:
            error_message = "Your password and confirm password didn't match!"
            return render(request, "register.html", {"error_message": error_message})

        else:
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()

            user = authenticate(request, username=uname, password=pass1)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                # Handle the case when authentication fails
                error_message = "Registration successful, but failed to log in. Please try logging in manually."
                return render(request, "login.html", {"error_message": error_message})

    return render(request, "register.html")


def Loginpage(request):
    if request.method == "POST":
        usrname = request.POST["user_name"]
        passw = request.POST["user_password"]
        user = authenticate(request, username=usrname, password=passw)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "Your username or password is incorrect."
            return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect("index")


@login_required(login_url=login)
def Homepage(request):
    return render(request, "home.html", {"user": request.user})


@login_required(login_url=login)
def ProfilePage(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        is_new_profile = False
    except Profile.DoesNotExist:
        profile = None
        is_new_profile = True
    success_message = None

    if request.method == "POST":
        user = request.user
        email = request.POST["email"]
        fullname = request.POST["full-name"]
        phone_number = request.POST["phone-number"]
        address = request.POST["address"]

        if is_new_profile:
            profile_data = Profile.objects.create(
                user=user,
                email=email,
                fullname=fullname,
                phone_number=phone_number,
                address=address,
            )
            success_message = "Profile saved sucessfully."
        else:
            profile.fullname = fullname
            profile.phone_number = phone_number
            profile.address = address
            profile.save()
            success_message = "Profile updated sucessfully."
        messages.success(request, success_message)
        return redirect("profile")

    context = {
        "user": request.user,
        "profile": profile,
        "is_new_profile": is_new_profile,
    }
    return render(request, "profile.html", context)
