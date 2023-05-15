from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import CustomerMessage

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
