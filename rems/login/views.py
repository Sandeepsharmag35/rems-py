from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError

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
            error = "Password must be at least 8 characters long including any Special Characters and Numeric Value!"
            return render(request, 'register.html', {'error': error})
        # End Of Validation

        # Username and Email Validation
        try:
            user = User.objects.create_user(username=uname, email=email, password=pass1)
        except IntegrityError as e:
            error_msg = str(e)
            if 'UNIQUE constraint failed: auth_user.email' in error_msg:
                error_msg = "Entered Email is already associated with other account, try another"
                return render(request, 'register.html', {'error_message_email': error_msg})
            elif 'UNIQUE constraint failed: auth_user.username' in error_msg:
                error_msg = "Username already taken, try another."
                return render(request, 'register.html', {'error_message_username': error_msg})
            
        # End Username and Email Validation

        pass2 = request.POST["form_cpassword"]

        if pass1 != pass2:
            error_message = "Your password and confirm password didn't match!"
            return render(request, 'register.html', {'error_message': error_message})

        else:
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()
            return redirect("login")
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
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect("index")


@login_required(login_url=login)
def Homepage(request):
    return render(request, "home.html", {'user': request.user}) 
