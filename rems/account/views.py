from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Profile
from app.models import Property
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def Indexpage(request):
    featured = Property.objects.filter(featured=True)
    context = {"featured": featured}
    return render(request, "index.html", context)


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
        username = request.POST["user_name"]
        passw = request.POST["user_password"]
        user = authenticate(request, username=username, password=passw)

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
    featured = Property.objects.filter(featured=True)
    context = {"featured": featured, "user": request.user}
    return render(request, "home.html", context)


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
        # Get form data using request.POST.get() to avoid potential errors
        username = request.POST.get("username")
        email = request.POST.get("email")
        fullname = request.POST.get("full-name")
        phone_number = request.POST.get("phone-number")
        address = request.POST.get("address")
        profile_picture = request.FILES.get("profile-picture")

        # Check if the username and email is already registered
        if username != user and User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken, try another.")
            return redirect("profile")

        if email != user.email and User.objects.filter(email=email).exists():
            messages.error(request, "This email address is already registered.")
            return redirect("profile")
        user.username = username
        user.email = email
        user.save()

        if is_new_profile:
            profile_data = Profile.objects.create(
                user=user,
                fullname=fullname,
                phone_number=phone_number,
                address=address,
                profile_picture=profile_picture,
            )
            success_message = "Profile saved successfully."
        else:
            profile.fullname = fullname
            profile.phone_number = phone_number
            profile.address = address
            if profile_picture:
                profile.profile_picture = profile_picture

            profile.save()

            success_message = "Profile updated successfully."

        messages.success(request, success_message)
        return redirect("profile")

    context = {
        "user": user,
        "profile": profile,
        "is_new_profile": is_new_profile,
    }
    return render(request, "profile.html", context)


@login_required(login_url=login)
def ChangePassword(request):
    if request.method == "POST":
        old_password = request.POST.get("old-password")
        new_password = request.POST.get("new-password")
        confirm_password = request.POST.get("confirm-password")

        try:
            validate_password(new_password)
        except ValidationError as error:
            error = "Your password must contain at least one special character (~!@#$%^&*()_+}{\":?><,./;') and one number."
            return render(request, "change_password.html", {"error": error})

        if not request.user.check_password(old_password):
            messages.error(request, "Your old password is incorrect.")
        elif new_password != confirm_password:
            messages.error(
                request, "The new password and confirmation password do not match."
            )
        else:
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(
                request, user
            )  # Update the session to prevent reauthentication
            success = "Your password has been successfully changed."
            return render(request, "change_password.html", {"success": success})

    return render(request, "change_password.html")
