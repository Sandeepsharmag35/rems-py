from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect("home")
#     else:
#         form = UserCreationForm()
#     return render(request, "signup.html", {"form": form})


def RegisterPage(request):
    if request.method == "POST":
        fullname = request.POST["form_name"]
        phonenum = request.POST["form_phone"]
        email = request.POST["form_email"]
        pass1 = request.POST["form_password"]
        pass2 = request.POST["form_password"]
        address = request.POST["form_address"]

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password didn't match!")

        else:
            myuser = User.objects.create_user(fullname, phonenum, email, pass1, address)
            myuser.save()
            return redirect("home")
    return render(request, "register.html")


def Loginpage(request):
    if request.method == "POST":
        email_id = request.POST["user_email"]
        passw = request.POST["user_password"]
        user = authenticate(request, email=email_id, password=passw)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Your password and confirm password are not same!")

    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect("home")


@login_required
def Homepage(request):
    user = request.user
    context = {"user": user}
    return render(request, "index.html", context)
